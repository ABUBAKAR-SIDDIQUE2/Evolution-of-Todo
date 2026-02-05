import sys
import pytest
from io import StringIO
from contextlib import redirect_stdout, redirect_stderr
from unittest.mock import patch
from src.cli import main, STORE

@pytest.fixture(autouse=True)
def reset_store():
    """Reset the global store before each test"""
    STORE._tasks.clear()
    STORE._next_id = 1

def run_cli_in_process(*args):
    """Run CLI main() in the same process to preserve global STORE state"""
    with patch("sys.argv", ["todo", *args]):
        out = StringIO()
        err = StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            try:
                main()
                exit_code = 0
            except SystemExit as e:
                exit_code = e.code
        
        return exit_code, out.getvalue(), err.getvalue()

def test_add_then_list():
    # Add
    code, out, _ = run_cli_in_process("add", "Persisted Task")
    assert code == 0
    assert "Task added" in out
    
    # List
    code, out, _ = run_cli_in_process("list", "--all")
    assert code == 0
    assert "Persisted Task" in out

def test_update_task():
    # Add
    run_cli_in_process("add", "Old Title")
    
    # Update
    code, out, _ = run_cli_in_process("update", "1", "--title", "New Title")
    assert code == 0
    assert "updated" in out
    
    # Verify
    code, out, _ = run_cli_in_process("list", "--all")
    assert "New Title" in out
    assert "Old Title" not in out

def test_update_task_not_found():
    code, out, _ = run_cli_in_process("update", "99", "--title", "Ghost")
    assert code == 1
    assert "Error: Task not found" in out

def test_delete_task():
    run_cli_in_process("add", "To Delete")
    
    code, out, _ = run_cli_in_process("delete", "1")
    assert code == 0
    assert "deleted" in out
    
    code, out, _ = run_cli_in_process("list", "--all")
    assert "To Delete" not in out

def test_delete_task_not_found():
    code, out, _ = run_cli_in_process("delete", "99")
    assert code == 1
    assert "Error: Task not found" in out

def test_toggle_task():
    run_cli_in_process("add", "Toggle Task")
    
    # Toggle to completed
    code, out, _ = run_cli_in_process("toggle", "1")
    assert code == 0
    assert "marked as Completed" in out
    
    # Verify in list
    code, out, _ = run_cli_in_process("list", "--completed")
    assert "Toggle Task" in out
    
    # Toggle back to pending
    code, out, _ = run_cli_in_process("toggle", "1")
    assert code == 0
    assert "marked as Pending" in out
    
    # Verify in list
    code, out, _ = run_cli_in_process("list", "--pending")
    assert "Toggle Task" in out

def test_toggle_task_not_found():
    code, out, _ = run_cli_in_process("toggle", "99")
    assert code == 1
    assert "Error: Task not found" in out