"""
File: fire.py
Name: Chris Lee
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename:
    :return:
    """
    return 0


def main():
    """
    The red spot of the image will appear and others will become
    grey scale.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


def highlight_fires(filename):
    old = SimpleImage(filename)
    for pixel in old:
        avg = (pixel.green+pixel.red+pixel.blue)//3
        if pixel.red > avg*HURDLE_FACTOR:
            pixel.red = 255
            pixel.blue = 0
            pixel.green = 0
        else:
            pixel.red = avg
            pixel.blue = avg
            pixel.green = avg
    return old


if __name__ == '__main__':
    main()
