import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    image = 255 - array
    plt.imshow(image)
    plt.axis('off')
    plt.show()
    return image


def ft_red(array) -> np.ndarray:
    """
    Keeps only the red color channel of the image.
    """
    image = array.copy()
    image[:, :, 1] = 0
    image[:, :, 2] = 0
    plt.imshow(image)
    plt.axis('off')
    plt.show()
    return image


def ft_green(array) -> np.ndarray:
    """
    Keeps only the green color channel of the image.
    """
    image = array.copy()
    image[:, :, 0] = 0
    image[:, :, 2] = 0
    plt.imshow(image)
    plt.axis('off')
    plt.show()
    return image


def ft_blue(array) -> np.ndarray:
    """
    Keeps only the blue color channel of the image.
    """
    image = array.copy()
    image[:, :, 0] = 0  # Setting red channel to 0
    image[:, :, 1] = 0  # Setting green channel to 0
    plt.imshow(image)
    plt.axis('off')
    plt.show()
    return image


def ft_grey(array) -> np.ndarray:
    """
    Converts the image to grayscale.
    """
    red_channel = array[:, :, 0] / 3
    green_channel = array[:, :, 1] / 3
    blue_channel = array[:, :, 2] / 3
    grey_channel = red_channel + green_channel + blue_channel
    grey_image = np.stack([grey_channel, grey_channel, grey_channel], axis=2)
    plt.imshow(grey_image.astype(np.uint8))
    plt.axis('off')
    plt.show()
    return grey_image.astype(np.uint8)
