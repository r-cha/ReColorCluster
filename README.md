# (Re)ColorClusters

## Installation

To set up a python virtual environment:

```bash
cd [directory where you cloned this repository]
python -m venv 'imagecluster'
source imagecluster/bin/activate
pip install -r requirements.txt
```

## Usage

### Prepare image

This process is nondestructive, so your photo is completely safe! That being said, if you have an image you like, you can copy the complete path of your image and paste it into the value of `INPUT_FILENAME` in `image_cluster.py`. Alternatively, copy and paste the image itself into the directory of this code, and put only the filename into the script. By default, the script expects `YOUR_IMAGE.JPG` in the same directory as the script itself.

To name change the name or location of the output image, change the value of `OUTPUT_FILENAME` in `image_cluster.py`. By default, the image will be saved in the directory of the script under the name `RESULT.PNG`.

Command line parameters are on the "Nice To Have" list...

### Run script

`python image_cluster.py`

This will downsample the color space of your image to 4 colors, then recolor it to the Polar Night palette of the [Nord Color Scheme](https://www.nordtheme.com/).

## Customization

This script is fairly flexible (aka barebones).

To recolor to different colors, change the value of `newcolors` in `image_cluster.py`. `newcolors` should be an array of hex colors in BGR format. If you only have RGB format, there is a function in `util.py` that can convert for you.

This script can also be used to find the "color scheme" of an image, sort of the `k` most common colors in the image. In this case, you'll want to remove any recoloring and simply return the list of `centers` after processing.

## Support

Again, some of this should be implemented as features but for now is just on the "Nice To Have" list... in other words this tool is not under active development. Regardless, let me know if you have any problems.
