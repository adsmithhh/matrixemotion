from emx.engine import Engine
from emx.io import load_emx
from pathlib import Path

def test_forward_progress():
    emx = load_emx(Path(__file__).parent.parent / "examples" / "base.yaml")
    eng = Engine(emx)
    s0 = eng.state.copy()
    s1 = eng.step()
    assert len(s1) == len(s0)
