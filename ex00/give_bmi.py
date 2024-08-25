import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI values based on height and weight.

    Args:
    - height (list): List of integers or floats representing heights.
    - weight (list): List of integers or floats representing weights.

    Returns:
    - list: List of BMI values calculated for each corresponding
      height and weight pair.
    """
    try:
        if len(height) != len(weight):
            raise ValueError("height and weight must be the same length")

        if not all(isinstance(h, (int, float)) for h in height):
            raise TypeError("All elements in height must be int or float")
        if not all(isinstance(w, (int, float)) for w in weight):
            raise TypeError("All elements in weight must be int or float")

        height_np = np.array(height, dtype=np.float64)
        weight_np = np.array(weight, dtype=np.float64)

        if np.any(height_np <= 0) or np.any(weight_np <= 0):
            raise ValueError("Height and weight must be greater than zero")

        bmi_np = weight_np / (height_np ** 2)
        return bmi_np.tolist()

    except (TypeError, ValueError) as error:
        print(f"An error occurred: {error}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a BMI limit and generate a list of booleans indicating whether
    each BMI value exceeds the limit.

    Args:
    - bmi (list): List of integers or floats representing BMI values.
    - limit (int): Limit value for BMI comparison.

    Returns:
    - list: List of booleans indicating whether each BMI value exceeds the
    specified limit.
    """
    try:
        bmi_np = np.array(bmi, dtype=np.float64)

        if not isinstance(limit, int):
            raise TypeError("limit must be an integer")

        above_limit = bmi_np > limit
        return above_limit.tolist()

    except TypeError as error:
        print(f"An error occurred: {error}")
        return []
