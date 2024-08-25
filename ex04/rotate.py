from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def print_rows_firstelem(arr, int_mode):
    length = arr.shape[0]
    for count, row in enumerate(arr):
        if count < 3 or count >= length - 3:
            if count == 0:
                if int_mode == 1:
                    print("[[[", row[0], "]", sep="")
                else:
                    print("[[", row[0], sep="")
            elif count == length - 1:
                if int_mode == 1:
                    print("  [", row[0], "]]]", sep="")
                else:
                    print("  ", row[0], "]]", sep="")
            else:
                if int_mode == 1:
                    print("  [", row[0], "]", sep="")
                else:
                    print("  ", row[0], sep="")
        if count == 2:
            print("  ...")


def rotate_image(image_array):
    """
    Rotate the input image array manually by transposing it.

    Parameters:
    image_array (numpy.ndarray): The input image array to be rotated.

    Returns:
    numpy.ndarray: The rotated image array.
    """
    height, width = image_array.shape
    rotated_image_array = np.zeros((width, height), dtype=image_array.dtype)

    for i in range(height):
        for j in range(width):
            rotated_image_array[j, i] = image_array[i, j]

    return rotated_image_array


def main():
    try:
        path = "animal.jpg"
        image_array = ft_load(path)

        if image_array.size == 0 or isinstance(image_array, str):
            raise AssertionError(f"Error: {image_array}")

        zoomed_image_array = image_array[100:500, 400:800, :]
        zoomed_image = Image.fromarray(zoomed_image_array)

        grayscale_image_array = np.array(zoomed_image.convert('L'))
        grayscale_shape = grayscale_image_array.shape
        grayscale_shape_channel = (grayscale_shape[0], grayscale_shape[1], 1)

        print(f"The shape of image is: {grayscale_shape_channel}"
              f" or {grayscale_shape}")
        print_rows_firstelem(grayscale_image_array, 1)

        rotated_image_array = rotate_image(grayscale_image_array)

        print(f"New shape after Transpose: {rotated_image_array.shape}")
        print(rotated_image_array)

        plt.imshow(rotated_image_array, cmap='gray')
        plt.axis('on')
        plt.show()

    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
