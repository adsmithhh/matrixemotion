from pathlib import Path
from typing import Any, Dict
import json, yaml

def load_emx(path: Path) -> Dict[str, Any]:
    data = yaml.safe_load(Path(path).read_text()) if path.suffix in {'.yml', '.yaml'} else json.loads(Path(path).read_text())
    # Basic shape checks (avoid heavy deps here).
    assert 'emx_version' in data
    assert 'emotions' in data and isinstance(data['emotions'], list)
    assert 'matrix' in data and isinstance(data['matrix'], list)
    assert 'params' in data and isinstance(data['params'], dict)
    return data
