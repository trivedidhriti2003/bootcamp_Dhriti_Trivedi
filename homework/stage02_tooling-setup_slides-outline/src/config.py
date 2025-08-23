import os
from dotenv import load_dotenv

def load_env():
    """
    Load environment variables from a .env file in the project root.
    """
    # Get the project root directory
    project_dir = os.path.join(os.path.dirname(__file__), '..')

    # Construct the path to the .env file
    dotenv_path = os.path.join(project_dir, '.env')

    # Load the .env file
    load_dotenv(dotenv_path)

def get_key(key_name):
    """
    Get a specific environment variable by its key name.

    Args:
        key_name (str): The name of the environment variable to retrieve.

    Returns:
        str: The value of the environment variable, or None if not found.
    """
    return os.getenv(key_name)