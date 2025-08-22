import sys
import yaml
from src.emx.core import EmotionalMatrix

# Example: load initial emotions
initial = {
    "joy": 0.7,
    "sadness": 0.1,
    "anger": 0.1,
    "fear": 0.1
}

# Simulate input (e.g., event)
input_matrix = {
    "joy": 0.5,
    "sadness": 0.2,
    "anger": 0.15,
    "fear": 0.15
}

emx = EmotionalMatrix(initial)
print("Before:", emx)
emx.step(input_matrix)
print("After: ", emx)