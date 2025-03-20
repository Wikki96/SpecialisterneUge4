import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from src.load_config import load_config

if __name__ == "__main__":
    config = load_config()
    print(config)
    print(config["pw"])
    assert isinstance(config["pw"], str)