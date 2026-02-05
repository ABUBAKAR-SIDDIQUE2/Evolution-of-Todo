import pytest
from src.store import TaskStore, Task

def test_add_task():
    store = TaskStore()
    task = store.add_task("Buy milk", description="2 liters")
    
    assert isinstance(task, Task)
    assert task.id == 1
    assert task.title == "Buy milk"
    assert task.description == "2 liters"
    assert task.completed is False
    assert task.created_at is not None
    assert task.updated_at is not None

def test_add_task_increments_id():
    store = TaskStore()
    t1 = store.add_task("First")
    t2 = store.add_task("Second")
    
    assert t1.id == 1
    assert t2.id == 2

def test_add_task_validation():
    store = TaskStore()
    with pytest.raises(ValueError):
        store.add_task("")

def test_list_tasks():
    store = TaskStore()
    t1 = store.add_task("One")
    t2 = store.add_task("Two")
    t2.completed = True
    
    all_tasks = store.list_tasks(status="all")
    assert len(all_tasks) == 2
    
    pending = store.list_tasks(status="pending")
    assert len(pending) == 1
    assert pending[0].id == 1
    
    completed = store.list_tasks(status="completed")
    assert len(completed) == 1
    assert completed[0].id == 2

def test_update_task():
    store = TaskStore()
    t1 = store.add_task("Old Title", description="Old Desc")
    
    updated = store.update_task(t1.id, title="New Title")
    assert updated.title == "New Title"
    assert updated.description == "Old Desc"
    assert updated.updated_at > t1.created_at

    updated2 = store.update_task(t1.id, description="New Desc")
    assert updated2.title == "New Title"
    assert updated2.description == "New Desc"

def test_update_task_not_found():
    store = TaskStore()
    with pytest.raises(ValueError, match="Task not found"):
        store.update_task(99, title="Ghost")

def test_delete_task():
    store = TaskStore()
    t1 = store.add_task("To Delete")
    
    deleted = store.delete_task(t1.id)
    assert deleted.id == t1.id
    
    assert len(store.list_tasks(status="all")) == 0

def test_delete_task_not_found():
    store = TaskStore()
    with pytest.raises(ValueError, match="Task not found"):
        store.delete_task(99)

def test_toggle_task():
    store = TaskStore()
    t1 = store.add_task("Toggle Me")
    assert t1.completed is False
    
    store.toggle_task(t1.id)
    assert t1.completed is True
    
    store.toggle_task(t1.id)
    assert t1.completed is False

def test_toggle_task_not_found():
    store = TaskStore()
    with pytest.raises(ValueError, match="Task not found"):
        store.toggle_task(99)
