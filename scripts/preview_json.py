
---

## **Python Script: preview_json.py**

Save this in `/scripts/preview_json.py`:

```python
#!/usr/bin/env python3
"""
preview_json.py
Preview AI workflow JSON fields, outputs, and commands.
"""

import json
import argparse
import os

def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def preview_fields(workflow):
    print(f"Workflow: {workflow.get('title', '<no title>')}")
    print(f"Description: {workflow.get('description', '<no description>')}\n")
    
    print("Fields:")
    for i, field in enumerate(workflow.get("fields", []), start=1):
        default = field.get("default", "")
        extra = ""
        if "min" in field and "max" in field and "step" in field:
            extra = f", min:{field['min']}, max:{field['max']}, step:{field['step']}"
        print(f"{i}. {field['id']} ({field['type']}) - {field.get('label', '')} [required: {field.get('required', False)}{extra}, default: {default}]")
    
    print("\nOutput:")
    for out in workflow.get("output", []):
        print(f"{out.get('id')} ({out.get('type')}, {out.get('format', 'N/A')})")

def preview_command(workflow):
    cmd = workflow.get("command")
    if cmd:
        print("\nCommand to run:")
        print(cmd)

def main():
    parser = argparse.ArgumentParser(description="Preview AI Workflow JSON")
    parser.add_argument("json_file", type=str, help="Path to workflow JSON file")
    parser.add_argument("--command", action="store_true", help="Only show command")
    args = parser.parse_args()

    if not os.path.exists(args.json_file):
        print(f"[ERROR] File not found: {args.json_file}")
        return

    workflow = load_json(args.json_file)

    if args.command:
        preview_command(workflow)
    else:
        preview_fields(workflow)
        preview_command(workflow)

if __name__ == "__main__":
    main()

