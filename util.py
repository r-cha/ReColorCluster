import cv2
import numpy as np

###
### File utils
###

def load_image(filename):
    """
    Load an image into a nparray
    """
    return cv2.imread(filename)

def save_image(filename, data, img):
    """
    Show a nparray as an image
    """

    data = data.reshape((img.shape))
    cv2.imwrite(filename, data)

def read_colorfile(filename:str):
    """
    Load a user-defined colorway.
    """
    colors = []
    with open(filename, 'r') as file:
        for color in file:
            colors.append(toTuple(color))
    return np.array(colors)

###
### Img utils
###

def img_to_ptlist(img):
    """
    Transform image into a list of pts
    """
    return img.reshape(-1, 3)

###
### Color utils
###

def color_selector(name, filename):
    if filename is not None:
        return read_colorfile(filename)
    else:
        load_included_colorway(name)

def load_included_colorway(name:str):
    params = name.split(".")
    if params[0] == "Nord":
        return getattr(Nord, params[1], Nord.polar_night)
    elif params[0] == "Horizon":
        return getattr(Horizon, params[1], Horizon.sunburst)
    else:
        # Panic state. The requested color class does not exist.
        return np.array([toTuple('#000000')])

def toTuple(hex):
    """
    Convert hex to BGR
    see https://stackoverflow.com/a/29643643
    """
    hex = hex.strip('#')
    return np.array([int(hex[4:6], 16), int(hex[2:4], 16), int(hex[0:2], 16) ])

###
### Included colorways
###

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

class Horizon:

    black = toTuple('#16161C')
    lessblack = toTuple('#1A1C23')
    midblack = toTuple('#1C1E26')
    upperblack = toTuple('#232530')
    stillblack = toTuple("#2E303E")
    brightblack = toTuple('#6C6F93')

    purple = toTuple('#B877DB')
    blue = toTuple('#25B2BC')
    red = toTuple('#E95678')
    orange1 = toTuple('#F09383')
    orange2 = toTuple('#FAB795')
    orange3 = toTuple('#FAC29A')

    dark_syntax = np.array([black, brightblack, purple, blue, red, orange1, orange2, orange3])
    sunburst = np.array([black, lessblack, midblack, upperblack, red, orange1, orange2, orange3])