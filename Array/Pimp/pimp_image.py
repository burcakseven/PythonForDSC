import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.array:
    '''
    Inverts the color of the image received
    '''
    new_image = 255 - array 
    plt.imshow(new_image)
    plt.show()
    return new_image

def ft_red(array) -> np.array:
    '''
    Returns the red color of the image received
    '''
    red_array = array.copy()
    red_array[:, :, 1:] = 0
    plt.imshow(red_array)
    plt.show()
    return red_array

def ft_green(array) -> np.array:
    '''
    Returns the green color of the image received
    '''
    green_array = array.copy()
    green_array[:, :, [0,2]] = 0
    plt.imshow(green_array)
    plt.show()
    return green_array

def ft_blue(array) -> np.array:
    '''
    Returns the blue color of the image received
    '''
    blue_array = array.copy()
    blue_array[:, :, :2] = 0
    plt.imshow(blue_array)
    plt.show()
    return blue_array

def ft_grey(array) -> np.array:
    '''
    Returns the grey color of the image received
    '''
    grey_array = array.copy()
    grey_array = np.mean(array, axis=2)
    plt.imshow(grey_array, cmap="gray")
    plt.show()
    return grey_array