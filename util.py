import cv2
import numpy as np
from matplotlib import pyplot as plt

def load_image(filename):
    """
    Load an image into a nparray
    """
    return cv2.imread(filename)

def img_to_ptlist(img):
    """
    Transform image into a list of pts
    """

    return img.reshape(-1, 3)

def save_image(filename, data, img):
    """
    Show a nparray as an image
    """

    data = data.reshape((img.shape))

    cv2.imwrite(filename, data)

def remap_colors(data, colors, newcolors):

    print(type(colors))
    print(type(newcolors))

    lut = {}
    for color in colors:
        lut[color] = newcolors
    for pt in data:
        pt = lut[pt]
    
    return data

def toTuple(hex):
    """
    Convert hex to BGR
    see https://stackoverflow.com/a/29643643
    """
    hex = hex.strip('#')
    return np.array([int(hex[4:6], 16), int(hex[2:4], 16), int(hex[0:2], 16) ])

class Nord:

    nord0 = toTuple('#2e3440')
    nord1 = toTuple('#3b4252')
    nord2 = toTuple('#434c5e')
    nord3 = toTuple('#4c566a')

    nord4 = toTuple('#d8dee9')
    nord5 = toTuple('#e5e9f0')
    nord6 = toTuple('#eceff4')

    nord7 = toTuple('#8fbcbb')
    nord8 = toTuple('#88c0d0')
    nord9 = toTuple('#81a1c1')
    nord10 = toTuple('#5e81ac')

    nord11 = toTuple('#bf616a')
    nord12 = toTuple('#d08770')
    nord13 = toTuple('#ebcb8b')
    nord14 = toTuple('#a3be8c')
    nord15 = toTuple('#b48ead')

    polar_night = np.array([nord0, nord1, nord2, nord3])
    snow_storm = np.array([nord4, nord5, nord6])
    frost = np.array([nord7, nord8, nord9, nord10])
    aurora = np.array([nord11, nord12, nord13, nord14, nord15])

    complete = np.concatenate((polar_night, snow_storm, frost, aurora))