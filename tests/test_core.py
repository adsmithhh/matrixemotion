from src.emx.core import EmotionalMatrix

def test_emotional_matrix_step():
    init = {"joy": 0.8, "sadness": 0.1}
    input_ = {"joy": 0.6, "sadness": 0.3}
    emx = EmotionalMatrix(init)
    emx.step(input_)
    assert abs(emx.emotions["joy"] - 0.78) < 1e-6
    assert abs(emx.emotions["sadness"] - 0.12) < 1e-6