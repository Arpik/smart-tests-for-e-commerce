import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Test if API key is loaded correctly
api_key = os.getenv("OPENAI_API_KEY")
print("API Key Loaded:", bool(api_key))


def load_config(file_path):
    """Load a JSON configuration file."""
    with open(file_path, 'r') as file:
        return json.load(file)
