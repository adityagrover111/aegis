import pytest
import json
from incident_loader import load_incidents

def test_missing_file():
    with pytest.raises(FileNotFoundError):
        load_incidents("data/does_not_exist.json")

def test_invalid_json(tmp_path):
    file_path=tmp_path / "broken.json"
    file_path.write_text("{invalid json}", encoding="utf-8")
    with pytest.raises(json.JSONDecodeError):
        load_incidents(file_path)