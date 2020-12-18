"""
File: shrink.py
Name: Chris Lee
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""


from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str,
    :return img: SimpleImage,
    """
    old = SimpleImage(filename)
    blank_image = SimpleImage.blank(old.width // 2, old.height // 2)
    blank_image.show()
    for x in range(old.width):
        for y in range(old.height):
            new = blank_image.get_pixel(x // 2, y // 2)
            old2 = old.get_pixel(x, y)
            if x % 2 == 0 and y % 2 == 0:
                new.green = old2.green
                new.blue = old2.blue
                new.red = old2.red
    return blank_image


def main():
    """
    The computer will decrease the picture size to 1/4
    without changing the structure of the image while
    viewing.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
