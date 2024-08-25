import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D array and print its shape.

    Args:
    - family (list): A 2D list representing the array
    to be sliced.
    - start (int): Starting index for slicing (inclusive).
    - end (int): Ending index for slicing (exclusive).

    Returns:
    - list: A sliced version of the 2D array based on the
    provided start and end indices.

    Raises:
    - TypeError: If 'family' is not a valid 2D list.
    - ValueError: If 'start' or 'end' indices are out of
    range or 'start' is greater than or equal to 'end'.
    """
    try:
        if not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError("Start and end must be integers")

        if not isinstance(family, list) \
                or not all(isinstance(row, list) for row in family):
            raise TypeError("Input must be a 2D list")

        if not all(len(item) == len(family[0]) for item in family):
            raise ValueError("Input list with different sizes")

        shape = np.array(family).shape

        if start < 0:
            start += shape[0]
        if end < 0:
            end += shape[0]
        if start < 0 or end > shape[0] or start >= end:
            raise ValueError("Invalid start or end indices")

        print(f"My shape is : {shape}")

        sliced_array = np.array(family)[start:end]
        print(f"My new shape is : {sliced_array.shape}")

        return np.array(family)[start:end].tolist()

    except (TypeError, ValueError, AssertionError) as error:
        print(f"{error.__class__.__name__}: {error}")
        return []
