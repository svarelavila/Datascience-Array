from PIL import Image
import numpy as np
import os


def ft_load(path: str) -> np.ndarray:
    """
    Loads a JPEG image from the specified path, converts it to a
    NumPy array, and handles several potential errors.

    Arguments:
    - path (str): The path of the JPEG image file.

    Returns:
    - np.ndarray: A NumPy array representing the loaded image,
    or an empty array if an error occurs.

    Raises:
    - AssertionError: If the file does not exist or is not a JPEG file.
    """
    try:
        if not os.path.exists(path):
            raise AssertionError(f"Error: File '{path}' not found.")

        if not path.lower().endswith(('.jpg', '.jpeg')):
            raise AssertionError(f"Error: '{path}' is not a JPEG file.")

        with Image.open(path) as img:
            img = img.convert("RGB")
            img_array = np.array(img)

            return img_array

    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return np.array([])
