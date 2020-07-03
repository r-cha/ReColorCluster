import argparse
import numpy as np
import cv2

from util import (
    load_image, 
    img_to_ptlist,
    save_image,
    color_selector
)

def main(args):
    """
    see https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_ml/py_kmeans/py_kmeans_opencv/py_kmeans_opencv.html
    """
    img = load_image(args.infile)
    Z = np.float32(img_to_ptlist(img))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 5, 1.0)
    newcolors = color_selector(args.colors, args.colorfile)
    K = len(newcolors)

    _, labels, centers = cv2.kmeans(Z,K,None,criteria,1,cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    res = newcolors[labels.flatten()]

    save_image(args.outfile, res, img)

def parse():
    parser = argparse.ArgumentParser(description="Recolor an image.")
    parser.add_argument("-i", "--infile", metavar="FILENAME", default="YOUR_IMAGE.JPG",
                        help="The filename of the image to recolor.")
    parser.add_argument("-o", "--outfile", metavar="FILENAME", default="RESULT.PNG",
                        help="The output filename of the new image.")
    parser.add_argument("-c", "--colors", metavar="COLORWAY", default="Nord.polar_night",
                        help="The name of the included colorscheme to use, e.g. Horizon.sunburst")
    parser.add_argument("-cf", "--colorfile", metavar="FILENAME", default=None,
                        help="The name of a file defining the new colors. \
                        This file must be a list (one value per line) of RGB hex values including the leading '#' character. \
                        If present, takes precedence over other arguments.")
    return parser.parse_args()

if __name__=="__main__":
    args = parse()
    main(args)