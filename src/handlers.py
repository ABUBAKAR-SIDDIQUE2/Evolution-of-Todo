from src.store import TaskStore
from src.utils import format_output

def add_task_handler(args, store: TaskStore) -> int:
    try:
        task = store.add_task(title=args.title, description=args.desc)
        print(f"Task added: [{task.id}] {task.title}")
        return 0
    except ValueError as e:
        print(f"Error: {e}")
        return 1

def list_tasks_handler(args, store: TaskStore) -> int:
    status = "pending"
    if args.all:
        status = "all"
    elif args.completed:
        status = "completed"
    
    tasks = store.list_tasks(status=status)
    fmt = "json" if args.json else "table"
    print(format_output(tasks, format_type=fmt))
    return 0

def update_task_handler(args, store: TaskStore) -> int:
    try:
        store.update_task(id=int(args.id), title=args.title, description=args.desc)
        print(f"Task [{args.id}] updated.")
        return 0
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1

def delete_task_handler(args, store: TaskStore) -> int:
    try:
        store.delete_task(id=int(args.id))
        print(f"Task [{args.id}] deleted.")
        return 0
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1

def toggle_task_handler(args, store: TaskStore) -> int:
    try:
        task = store.toggle_task(id=int(args.id))
        status = "Completed" if task.completed else "Pending"
        print(f"Task [{args.id}] marked as {status}.")
        return 0
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1