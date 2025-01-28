import json

def load_config(file_path):
    """Load a JSON configuration file."""
    with open(file_path, 'r') as file:
        return json.load(file)