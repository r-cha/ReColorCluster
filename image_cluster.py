import numpy as np
import cv2

from util import (
    load_image, 
    img_to_ptlist, 
    remap_colors, 
    save_image,
    Nord
)


def main():
    """
    see https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_ml/py_kmeans/py_kmeans_opencv/py_kmeans_opencv.html
    """

    img = load_image("YOUR_IMAGE.JPG")
    Z = img_to_ptlist(img)
    Z = np.float32(Z)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 5, 1.0)
    K = 4
    ret,label,center=cv2.kmeans(Z,K,None,criteria,1,cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    newcolors = Nord.polar_night
    res = newcolors[label.flatten()]

    # res2 = remap_colors(res, center, newcolors)

    save_image("RESULT.PNG", res, img)

if __name__=="__main__":
    main()