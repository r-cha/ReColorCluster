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
    if args.like is not None:
        _, newcolors = cluster_image(args.likefile, args.k)
    else:
        newcolors = color_selector(args.colors, args.colorfile)
    K = len(newcolors)

    labels, _ = cluster_image(args.infile, len(newcolors))
    res = newcolors[labels.flatten()]

    img = load_image(args.infile)
    save_image(args.outfile, res, img)

def cluster_image(infile:str, K:int):
    img = load_image(infile)
    Z = np.float32(img_to_ptlist(img))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 5, 1.0)

    _, labels, centers = cv2.kmeans(Z,K,None,criteria,1,cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)

    return labels, centers

def parse():
    parser = argparse.ArgumentParser(description="Recolor an image.")
    parser.add_argument("-i", "--infile", metavar="FILENAME", default="YOUR_IMAGE.JPG",
                        help="The filename of the image to recolor.")
    parser.add_argument("-o", "--outfile", metavar="FILENAME", default="RESULT.PNG",
                        help="The output filename of the new image.")
    parser.add_argument("-cp", "--compress", metavar="K", default=None,
                        help="Recolor the image based on its own K most common colors.")
    parser.add_argument("-cw", "--colorway", metavar="COLORWAY", default="Nord.polar_night",
                        help="The name of the included colorscheme to use, e.g. Horizon.sunburst")
    parser.add_argument("-cf", "--colorfile", metavar="FILENAME", default=None,
                        help="The name of a file defining the new colors. \
                        This file must be a list (one value per line) of RGB hex values including the leading '#' character. \
                        If present, takes precedence over other arguments.")
    parser.add_argument("-l", "--like", default=None, nargs=2,
                        help="An image to use as the basis for recoloring, followed by the number of colors to use. \
                        Specifying this option with an image filename will select the K common colors from the 'like' file \
                        And use them as the color scheme for the infile.")
    namespace = parser.parse_args()

    if namespace.compress is not None:
        namespace.like = (namespace.infile, namespace.compress)
    if namespace.like is not None:
        namespace.__setattr__("likefile", namespace.like[0])
        namespace.__setattr__("k", int(namespace.like[1]))

    return namespace

if __name__=="__main__":
    args = parse()
    main(args)