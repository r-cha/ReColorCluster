import numpy as np
import cv2

from util import (
    load_image, 
    img_to_ptlist, 
    remap_colors, 
    save_image,
    Nord,
    Horizon
)


INPUT_FILENAME = "YOUR_IMAGE.JPG"
OUTPUT_FILENAME = "RESULT.PNG"

def main():
    """
    see https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_ml/py_kmeans/py_kmeans_opencv/py_kmeans_opencv.html
    """

    img = load_image(INPUT_FILENAME)
    Z = np.float32(img_to_ptlist(img))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 5, 1.0)
    newcolors = Nord.polar_night # This determines the colors present in the final image
    K = len(newcolors)

    ret, labels, centers = cv2.kmeans(Z,K,None,criteria,1,cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    res = newcolors[labels.flatten()]

    save_image(OUTPUT_FILENAME, res, img)

if __name__=="__main__":
    main()