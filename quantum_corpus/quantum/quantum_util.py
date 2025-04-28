"""Utilities for Quantum package."""


def complex_addition(a: list[int], b: list[int]) -> str:
    """Complex addition of two complex numbers.

    Args:
    -----
        a: First complex number in the form (a + bi).
        b: Second complex number in the form (c + di).

    Returns
    -------
        Complex number representing the sum (k + ni).

    """
    term_1 = a[0] + b[0]
    term_2 = a[1] + b[1]

    return f"{term_1} + {term_2}i"


def complex_multiplication(a: list[int], b: list[int]) -> str:
    """Complex multiplication of two complex numbers.

    Args:
    -----
        a: First complex number in the form (a + bi).
        b: Second complex number in the form (c + di).

    Returns
    -------
        Complex number representing the sum (k + ni).

    """
    term_1 = (a[0] * b[0]) - (a[1] * b[1])
    term_2 = (a[0] * b[1]) + (a[1] * b[0])

    return f"{term_1} + {term_2}i"
