import json
from dataclasses import asdict
from datetime import datetime

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

def format_output(tasks, format_type="table"):
    if format_type == "json":
        data = [asdict(t) for t in tasks]
        return json.dumps(data, default=json_serial, indent=2)
    
    if not tasks:
        return "No tasks found"
    
    # Simple table formatting
    header = f"{'ID':<4} | {'Title':<30} | {'Status':<10} | {'Created':<20}"
    separator = "-" * len(header)
    lines = [header, separator]
    
    for t in tasks:
        status = "Completed" if t.completed else "Pending"
        created = t.created_at.strftime("%Y-%m-%d %H:%M:%S")
        lines.append(f"{t.id:<4} | {t.title[:30]:<30} | {status:<10} | {created:<20}")
    
    return "\n".join(lines)
