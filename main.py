import os
from src.build import build

if __name__ == "__main__":
    build(os.path.dirname(os.path.realpath(__file__)))
