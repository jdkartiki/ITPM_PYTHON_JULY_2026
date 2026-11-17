import json
import os

def read_file(path):
    # If file does not exist, return empty list
    if not os.path.exists(path):
        return []

    try:
        with open(path, "r") as f:
            content = f.read().strip()

            # If file is empty, return empty list
            if not content:
                return []

            return json.loads(content)

    except json.JSONDecodeError:
        # If JSON is invalid/corrupted
        print("Warning: JSON file is empty or corrupted. Resetting file...")
        return []


def write_file(path, data):
    # Ensure directory exists
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w") as f:
        json.dump(data, f, indent=4)
