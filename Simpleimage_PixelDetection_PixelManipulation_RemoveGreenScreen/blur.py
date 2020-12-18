"""
File: blur.py
Name: Chris Lee
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def main():
    """
    The computer will make the imported image blur depending
    on how many times the input is.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


def blur(img):
    blank_image = SimpleImage.blank(img.width, img.height)
    for j in range(img.height-1):
        for i in range(img.width-1):
            new_pixel = blank_image.get_pixel(i, j)
            if i == 0 and j == 0:
                left_corner1 = img.get_pixel(i, j)
                left_corner2 = img.get_pixel(i, j+1)
                left_corner3 = img.get_pixel(i+1, j)
                left_corner4 = img.get_pixel(i+1, j+1)
                left_corner_green = (left_corner1.green+left_corner2.green+left_corner3.green+left_corner4.green) // 4
                left_corner_red = (left_corner1.red+left_corner2.red+left_corner3.red+left_corner4.red) // 4
                left_corner_blue = (left_corner1.blue+left_corner2.blue+left_corner3.blue+left_corner4.blue) // 4
                new_pixel.green = left_corner_green
                new_pixel.blue = left_corner_blue
                new_pixel.red = left_corner_red
            elif 0 < i < (img.width-1) and j == 0:
                upper1 = img.get_pixel(i, j)
                upper2 = img.get_pixel(i-1, j)
                upper3 = img.get_pixel(i+1, j)
                upper4 = img.get_pixel(i, j+1)
                upper5 = img.get_pixel(i-1, j+1)
                upper6 = img.get_pixel(i-1, j+1)
                upper_green = (upper1.green+upper2.green+upper3.green+upper4.green+upper5.green+upper6.green) // 6
                upper_red = (upper1.red+upper2.red+upper3.red+upper4.red+upper5.red+upper6.red) // 6
                upper_blue = (upper1.blue+upper2.blue+upper3.blue+upper4.blue+upper5.blue+upper6.blue) // 6
                new_pixel.green = upper_green
                new_pixel.blue = upper_blue
                new_pixel.red = upper_red
            elif i == img.width and j == 0:
                right_corner1 = img.get_pixel(i, j)
                right_corner2 = img.get_pixel(i-1, j)
                right_corner3 = img.get_pixel(i, j+1)
                right_corner4 = img.get_pixel(i-1, j+1)
                right_corner_green = (right_corner1.green+right_corner2.green+right_corner3.green+right_corner4.green) // 4
                right_corner_red = (right_corner1.red+right_corner2.red+right_corner3.red+right_corner4.red) // 4
                right_corner_blue = (right_corner1.blue+right_corner2.blue+right_corner3.blue+right_corner4.blue) // 4
                new_pixel.green = right_corner_green
                new_pixel.blue = right_corner_blue
                new_pixel.red = right_corner_red
            elif i == 0 and 0 < j < img.height:
                left1 = img.get_pixel(i, j)
                left2 = img.get_pixel(i, j-1)
                left3 = img.get_pixel(i, j+1)
                left4 = img.get_pixel(i+1, j-1)
                left5 = img.get_pixel(i+1, j)
                left6 = img.get_pixel(i+1, j+1)
                left_green = (left1.green+left2.green+left3.green+left4.green+left5.green+left6.green) // 6
                left_blue = (left1.blue+left2.blue+left3.blue+left4.blue+left5.blue+left6.blue) // 6
                left_red = (left1.red+left2.red+left3.red+left4.red+left5.red+left6.red) // 6
                new_pixel.green = left_green
                new_pixel.blue = left_blue
                new_pixel.red = left_red
            elif i == img.width and 0 < j < img.height:
                right1 = img.get_pixel(i, j)
                right2 = img.get_pixel(i, j-1)
                right3 = img.get_pixel(i, j+1)
                right4 = img.get_pixel(i-1, j-1)
                right5 = img.get_pixel(i-1, j)
                right6 = img.get_pixel(i-1, j+1)
                right_green = (right1.green+right2.green+right3.green+right4.green+right5.green+right6.green) // 6
                right_blue = (right1.blue+right2.blue+right3.blue+right4.blue+right5.blue+right6.blue) // 6
                right_red = (right1.red+right2.red+right3.red+right4.red+right5.red+right6.red) // 6
                new_pixel.green = right_green
                new_pixel.blue = right_blue
                new_pixel.red = right_red
            elif i == 0 and j == img.height:
                left_low_corner1 = img.get_pixel(i, j)
                left_low_corner2 = img.get_pixel(i+1, j)
                left_low_corner3 = img.get_pixel(i, j-1)
                left_low_corner4 = img.get_pixel(i+1, j-1)
                left_low_corner_green = (left_low_corner1.green + left_low_corner2.green + left_low_corner3.green + left_low_corner4.green) // 4
                left_low_corner_red = (left_low_corner1.red + left_low_corner2.red + left_low_corner3.red + left_low_corner4.red) // 4
                left_low_corner_blue = (left_low_corner1.blue + left_low_corner2.blue + left_low_corner3.blue + left_low_corner4.blue) // 4
                new_pixel.green = left_low_corner_green
                new_pixel.blue = left_low_corner_blue
                new_pixel.red = left_low_corner_red
            elif 0 < i < (img.width-1) and j == img.height:
                lower1 = img.get_pixel(i, j)
                lower2 = img.get_pixel(i-1, j)
                lower3 = img.get_pixel(i+1, j)
                lower4 = img.get_pixel(i, j-1)
                lower5 = img.get_pixel(i-1, j-1)
                lower6 = img.get_pixel(i-1, j-1)
                lower_green = (lower1.green + lower2.green + lower3.green + lower4.green + lower5.green + lower6.green) // 6
                lower_red = (lower1.red + lower2.red + lower3.red + lower4.red + lower5.red + lower6.red) // 6
                lower_blue = (lower1.blue + lower2.blue + lower3.blue + lower4.blue + lower5.blue + lower6.blue) // 6
                new_pixel.green = lower_green
                new_pixel.blue = lower_blue
                new_pixel.red = lower_red
            elif i == img.width and j == img.height:
                right_low_corner1 = img.get_pixel(i, j)
                right_low_corner2 = img.get_pixel(i-1, j)
                right_low_corner3 = img.get_pixel(i, j-1)
                right_low_corner4 = img.get_pixel(i-1, j-1)
                right_low_corner_green = (right_low_corner1.green + right_low_corner2.green + right_low_corner3.green + right_low_corner4.green) // 4
                right_low_corner_red = (right_low_corner1.red + right_low_corner2.red + right_low_corner3.red + right_low_corner4.red) // 4
                right_low_corner_blue = (right_low_corner1.blue + right_low_corner2.blue + right_low_corner3.blue + right_low_corner4.blue) // 4
                new_pixel.green = right_low_corner_green
                new_pixel.blue = right_low_corner_blue
                new_pixel.red = right_low_corner_red
            else:
                middle1 = img.get_pixel(i, j)
                middle2 = img.get_pixel(i-1, j-1)
                middle3 = img.get_pixel(i, j-1)
                middle4 = img.get_pixel(i+1, j-1)
                middle5 = img.get_pixel(i-1, j)
                middle6 = img.get_pixel(i+1, j)
                middle7 = img.get_pixel(i-1, j+1)
                middle8 = img.get_pixel(i, j+1)
                middle9 = img.get_pixel(i+1, j+1)
                middle_green = (middle1.green + middle2.green + middle3.green + middle4.green + middle5.green + middle6.green + middle7.green + middle8.green + middle9.green) // 9
                middle_red = (middle1.red + middle2.red + middle3.red + middle4.red + middle5.red + middle6.red + middle7.red + middle8.red + middle9.red) // 9
                middle_blue = (middle1.blue + middle2.blue + middle3.blue + middle4.blue + middle5.blue + middle6.blue + middle7.blue + middle8.blue + middle9.blue) // 9
                new_pixel.green = middle_green
                new_pixel.blue = middle_blue
                new_pixel.red = middle_red
    return blank_image


if __name__ == '__main__':
    main()
