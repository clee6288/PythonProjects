"""
File: green_screen.py
Name: Chris Lee
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, the background image
    :param figure_img: SimpleImage, green screen figure image
    :return: SimpleImage, combined image
    """
    for y in range(background_img.height):
        for x in range(background_img.width):
            pixel_figure = figure_img.get_pixel(x, y)
            # avg = (pixel_figure.red + pixel_figure.blue + pixel_figure.green) // 3
            bigger = max(pixel_figure.red, pixel_figure.blue)
            if pixel_figure.green > bigger*2:
                pixel_background = background_img.get_pixel(x, y)
                pixel_figure.red = pixel_background.red
                pixel_figure.blue = pixel_background.blue
                pixel_figure.green = pixel_background.green
    return figure_img


def main():
    """
    Combine two images, one image that is green screen with figure and one image that is
    background picture.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
