from __future__ import annotations
from typing import List, Dict
import math

def _act(x: float, kind: str) -> float:
    if kind == 'identity':
        return x
    if kind == 'tanh':
        return math.tanh(x)
    if kind == 'sigmoid':
        return 1.0 / (1.0 + math.exp(-x))
    raise ValueError(f'Unknown nonlinearity: {kind}')

class Engine:
    def __init__(self, emx: Dict):
        self.emx = emx
        self.names = emx['emotions']
        self.index = {n:i for i,n in enumerate(self.names)}
        self.W = emx['matrix']
        self.decay = emx['params'].get('decay', 0.0)
        self.dt = emx['params'].get('dt', 0.1)
        self.temp = emx['params'].get('temperature', 1.0)
        self.kind = emx['params'].get('nonlinearity', 'identity')
        self.caps = emx['params'].get('caps', [1.0]*len(self.names))
        self.inhibitors = emx['params'].get('inhibitors', [])
        self.state = emx.get('initial_state', [0.0]*len(self.names))
        assert len(self.state) == len(self.names)
        assert all(len(row) == len(self.names) for row in self.W)

    def step(self, state: List[float] | None = None) -> List[float]:
        if state is None:
            state = self.state
        n = len(self.names)
        influ = [0.0]*n
        # Apply inhibitors as multiplicative masks on routes j->i
        # Build a per-edge mask M[i][j] in a lazy way.
        masks = [[1.0]*n for _ in range(n)]
        for rule in self.inhibitors:
            j = self.index.get(rule['source'])
            i = self.index.get(rule['target'])
            if i is not None and j is not None:
                masks[i][j] *= max(0.0, min(1.0, rule['factor']))

        # Influence accumulation
        for i in range(n):
            s = 0.0
            for j in range(n):
                s += self.W[i][j] * state[j] * masks[i][j]
            influ[i] = s

        # Euler step with decay and nonlinearity
        new_state = [0.0]*n
        for i in range(n):
            x = state[i] + self.dt * ( -self.decay*state[i] + self.temp * _act(influ[i], self.kind) )
            # clamp to [0, cap_i]
            x = max(0.0, min(self.caps[i], x))
            new_state[i] = x

        self.state = new_state
        return new_state
