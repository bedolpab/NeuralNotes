"""Cryptography notes package."""

from crypto import generate_n_length_binary

try:
    __all__ = [
        "generate_n_length_binary",
    ]
except ImportError as e:
    print(
        f"Warning: Unable to import functions from 'cryptography' package: {e}"
    )
    __all__ = [""]

if __name__ == "__main__":
    print(f"Running {__file__} directly.")
