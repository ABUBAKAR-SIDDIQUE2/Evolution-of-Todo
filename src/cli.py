import argparse
import logging
import sys
from src.store import TaskStore
from src.handlers import (
    add_task_handler, 
    list_tasks_handler, 
    update_task_handler, 
    delete_task_handler,
    toggle_task_handler
)

# Global store for the process lifetime
STORE = TaskStore()

def main():
    parser = argparse.ArgumentParser(description="Todo CLI")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable debug logging")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add Task Command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument("--desc", help="Task description")
    
    # List Tasks Command
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("--all", action="store_true", help="Show all tasks")
    list_parser.add_argument("--pending", action="store_true", help="Show pending tasks")
    list_parser.add_argument("--completed", action="store_true", help="Show completed tasks")
    list_parser.add_argument("--json", action="store_true", help="Output JSON")
    
    # Update Task Command
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id", help="Task ID")
    update_parser.add_argument("--title", help="New title")
    update_parser.add_argument("--desc", help="New description")

    # Delete Task Command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", help="Task ID")

    # Toggle Task Command
    toggle_parser = subparsers.add_parser("toggle", help="Toggle task completion")
    toggle_parser.add_argument("id", help="Task ID")
    
    args = parser.parse_args()
    
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format="%(message)s")
    
    exit_code = 0
    if args.command == "add":
        exit_code = add_task_handler(args, STORE)
    elif args.command == "list":
        exit_code = list_tasks_handler(args, STORE)
    elif args.command == "update":
        exit_code = update_task_handler(args, STORE)
    elif args.command == "delete":
        exit_code = delete_task_handler(args, STORE)
    elif args.command == "toggle":
        exit_code = toggle_task_handler(args, STORE)
    elif args.command is None:
        parser.print_help()
        exit_code = 1
    
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
