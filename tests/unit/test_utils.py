import json
from datetime import datetime, timezone
from src.utils import format_output
from src.store import Task

def test_format_output_json():
    now = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    task = Task(id=1, title="Test", created_at=now, updated_at=now)
    
    output = format_output([task], format_type="json")
    data = json.loads(output)
    
    assert len(data) == 1
    assert data[0]["id"] == 1
    assert data[0]["title"] == "Test"
    assert "2023-01-01" in data[0]["created_at"]

def test_format_output_table():
    now = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    task = Task(id=1, title="Test Task", created_at=now, updated_at=now)
    
    output = format_output([task], format_type="table")
    
    assert "ID" in output
    assert "Title" in output
    assert "1" in output
    assert "Test Task" in output
    assert "Pending" in output

def test_format_output_empty():
    assert "No tasks found" in format_output([], format_type="table")
    assert "[]" == format_output([], format_type="json")
