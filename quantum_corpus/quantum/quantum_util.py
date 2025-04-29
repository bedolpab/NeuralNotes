"""Utilities for Quantum package."""


def complex_addition(a: list[int], b: list[int]) -> str:
    """Complex addition of two complex numbers.

    Args:
    -----
        a: First complex number in the form (a + bi).
        b: Second complex number in the form (c + di).

    Returns
    -------
        Complex number representing the result (k + ni).

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
        Complex number representing the result (k + ni).

    """
    term_1 = (a[0] * b[0]) - (a[1] * b[1])
    term_2 = (a[0] * b[1]) + (a[1] * b[0])

    return f"{term_1} + {term_2}i"


def complex_division(a: list[int], b: list[int]) -> str:
    """Complex division of two complex numbers.

    Args:
    -----
        a: First complex number in the form (a + bi).
        b: Second complex number in the form (c + di).

    Returns
    -------
        Complex number representing the result (k + ni).

    """
    term_1_numerator = (a[0] * b[0]) + (a[1] * b[1])
    term_2_numerator = (b[0] * a[1]) - (a[0] * b[1])

    denominator = (b[0] ** 2) + (b[1] ** 2)

    term_1 = term_1_numerator / denominator
    term_2 = term_2_numerator / denominator

    return f"{term_1} + {term_2}i"
