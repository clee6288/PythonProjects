"""
File: mirror_lake.py
Name: Chris Lee
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename:
    :return:
    """
    return 0


def main():
    """
    The computer will create an mirror-like image.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


def reflect(filename):
    old = SimpleImage(filename)
    blank_img = SimpleImage.blank(old.width, old.height * 2)
    blank_img.show()
    for x in range(old.width):
        for y in range(old.height):
            #data
            img_pixel = old.get_pixel(x, y)

            #Empty Pixel 1
            new_pixel_1 = blank_img.get_pixel(x, y)

            #Empty pixel 2
            new_pixel_2 = blank_img.get_pixel(x, blank_img.height-1-y)

            new_pixel_1.green = img_pixel.green
            new_pixel_1.blue = img_pixel.blue
            new_pixel_1.red = img_pixel.red

            new_pixel_2.green = img_pixel.green
            new_pixel_2.blue = img_pixel.blue
            new_pixel_2.red = img_pixel.red
    return blank_img

if __name__ == '__main__':
    main()
