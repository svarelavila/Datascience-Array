from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def print_rows_firstelem(arr, int_mode):
    """
    Print a formatted display of the first elements
    in each row of a given array.

    Parameters:
    arr (array-like): The input array containing elements to be displayed.
    int (int): An integer specifying the display format: 0 for single brackets,
    1 for triple brackets.

    Iterates through the rows of the input array and displays the first
    elements of each row in a formatted manner. The display format is
    determined by the 'int' parameter. For 'int' equal to 0, single
    brackets are used to enclose the elements, while for 'int' equal
    to 1, triple brackets are used.
    """

    count = 0
    for row in arr:
        count += 1
    length = count
    count = 0
    for row in arr:
        if count == 0:
            if int_mode == 1:
                print("[[[", row[0], "]", sep="")
            else:
                print("[[", row[0], sep="")
        if count > 0 and count < 3 or count > length - 4:
            if int_mode == 1:
                if count == length - 1:
                    print("  [", row[0], "]]]", sep="")
                elif count < length - 1:
                    print("  [", row[0], "]", sep="")
            else:
                if count == length - 1:
                    print("  ", row[0], "]]", sep="")
                else:
                    print("  ", row[0], sep="")
        if count == 2:
            print("  ...")
        count += 1


def main():
    """
    Load, process, and display an image based on command-line arguments.

    This function serves as the main entry point of the script. It loads an
    image from the command-line argument, performs various image processing
    operations, and displays the resulting images. The script supports
    cropping, grayscale conversion, and zoomed image display. Errors related
    to file format and existence are caught and displayed.
    """
    try:
        path = "animal.jpg"
        image_array = ft_load(path)

        if image_array.size == 0 or isinstance(image_array, str):
            raise AssertionError(f"Error: {image_array}")

        print_rows_firstelem(image_array, 1)

        zoomed_image_array = image_array[100:500, 400:800, :]
        zoomed_image = Image.fromarray(zoomed_image_array)

        grayscale_image_array = np.array(zoomed_image.convert('L'))
        grayscale_shape = grayscale_image_array.shape
        grayscale_shape_channel = (grayscale_shape[0], grayscale_shape[1], 1)
        print(f"New shape after slicing: {grayscale_shape_channel}"
              f" or {grayscale_shape}")
        print_rows_firstelem(grayscale_image_array, 1)

        plt.imshow(grayscale_image_array, cmap='gray')
        plt.xticks(np.arange(0, 400, 50))
        plt.yticks(np.arange(0, 400, 50))
        plt.axis('on')
        plt.show()

    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
