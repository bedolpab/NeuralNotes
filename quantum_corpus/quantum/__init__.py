"""Quantum notes package."""

from quantum import *

try:
    __all__ = [
        "",
    ]
except ImportError as e:
    print(f"Warning: Unable to import functions from 'quantum' package: {e}")
    __all__ = [""]

if __name__ == "__main__":
    print(f"Running {__file__} directly.")
