#!/usr/bin/env python3
"""
validate_json.py
Validate all JSON workflow files in /models/ and /examples/ against the workflow schema.
"""

import json
import os
from jsonschema import validate, ValidationError

# Paths
SCHEMA_FILE = os.path.join(os.path.dirname(__file__), "../schemas/workflow.schema.json")
MODELS_DIR = os.path.join(os.path.dirname(__file__), "../models")
EXAMPLES_DIR = os.path.join(os.path.dirname(__file__), "../examples")


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_file(json_file, schema):
    try:
        data = load_json(json_file)
        validate(instance=data, schema=schema)
        print(f"[OK] {json_file}")
        return True
    except ValidationError as e:
        print(f"[ERROR] {json_file}: {e.message}")
        return False
    except json.JSONDecodeError as e:
        print(f"[ERROR] {json_file}: Invalid JSON - {e}")
        return False


def main():
    # Load schema
    try:
        schema = load_json(SCHEMA_FILE)
    except Exception as e:
        print(f"[FATAL] Cannot load schema: {e}")
        return

    all_files = []

    # Gather all JSON files
    for folder in [MODELS_DIR, EXAMPLES_DIR]:
        if os.path.exists(folder):
            for file_name in os.listdir(folder):
                if file_name.endswith(".json"):
                    all_files.append(os.path.join(folder, file_name))

    if not all_files:
        print("[INFO] No JSON files found to validate.")
        return

    # Validate each file
    success = True
    for json_file in all_files:
        if not validate_file(json_file, schema):
            success = False

    if success:
        print("\nAll JSON files are valid ✅")
    else:
        print("\nSome JSON files have errors ❌")


if __name__ == "__main__":
    main()

