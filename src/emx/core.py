"""
EMX Core Engine: Emotional Mixing Matrix

Implements Plutchik's eight primary emotions as a mutable, interactive matrix.
"""

import yaml

PLUTCHIK_EMOTIONS = [
    "joy", "sadness", "acceptance", "disgust", "fear", "anger", "surprise", "anticipation"
]

class EmotionalMatrix:
    def __init__(self, values=None):
        # Initialize emotions to 0.0 if not provided
        self.emotions = {e: 0.0 for e in PLUTCHIK_EMOTIONS}
        if values:
            for e in PLUTCHIK_EMOTIONS:
                if e in values:
                    self.emotions[e] = values[e]

    def step(self, input_matrix):
        # Simple update rule: blend current and input emotions, with clamping
        for e in PLUTCHIK_EMOTIONS:
            delta = input_matrix.get(e, 0.0) - self.emotions[e]
            # "Mutate" emotion slightly toward input
            self.emotions[e] += 0.1 * delta
            # Clamp between 0 and 1
            self.emotions[e] = min(max(self.emotions[e], 0.0), 1.0)

    def to_dict(self):
        return dict(self.emotions)

    def __repr__(self):
        return f"EmotionalMatrix({self.emotions})"

def load_matrix_from_yaml(path):
    with open(path) as f:
        data = yaml.safe_load(f)
    return EmotionalMatrix(data.get("emotions", {}))