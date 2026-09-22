import json


def save_json(file_path, data):
    """Save data to a JSON file."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def load_json(file_path):
    """Load and return data from a JSON file."""
    with open(file_path, "r") as file:
        return json.load(file)