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

This process is nondestructive, so your photo is completely safe!

If you have an image you like, provide the path to it in the `--infile` argument on the command line. Alternatively, copy and paste the image itself into the directory of this code and rename it `YOUR_IMAGE.JPG`.

To name change the name or location of the output image, specify the `--outfile` argument on the command line. By default, the image will be saved in the directory of the script under the name `RESULT.PNG`.

### Run script

`python image_cluster.py`

This will downsample the color space of your image to 4 colors, then recolor it to the Polar Night palette of the [Nord Color Scheme](https://www.nordtheme.com/).

## Customization

To recolor to different colors,

a) specify the `--colors` argument on the command line. This parameter must match the name of a colorway in `utils.py` (a black image result indicates that the requested colorway is not built-in). OR
b) specify the `--colorfile` argument on the command line. This parameter must be the filename of a color file, which is a simple file consisting of a list of RGB hex values, including the leading '#' character.

## Support

Again, some of this should be implemented as features but for now is just on the "Nice To Have" list... in other words this tool is not under active development. Regardless, let me know if you have any problems.
