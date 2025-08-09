from emx.engine import Engine
from emx.io import load_emx
from pathlib import Path

emx = load_emx(Path(__file__).parent / "base.yaml")
eng = Engine(emx)

state = eng.state.copy()
for t in range(10):
    state = eng.step(state)
    print(f"t={t+1:02d} ->", [round(x, 3) for x in state])
