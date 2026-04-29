from image import Image
import numpy as np


def adjust_brightness(image, factor):
    # when we brighten, we just want to make each channel higher by some amount
    # factor is a value > 0, how much you want to brighten the image by (< 1 = darken, > 1 = brighten)
    # non vectorized way
    x_pixels, y_pixels, channels = image.array.shape
    temp_img = Image(x_pixels, y_pixels, channels)

    # for x in range(x_pixels):
    #     for y in range(y_pixels):
    #         for c in range(channels):
    #             temp_img.array[x,y,c] = image.array[x,y,c] * factor

    # vectorized way
    temp_img.array = image.array * factor
    return temp_img


def adjust_contrast(image, factor, mid):
    # adjust the contrast by increasing the difference from the user-defined midpoint by factor amount
    x_pixels, y_pixels, channels = image.array.shape
    temp_img = Image(x_pixels, y_pixels, channels)
    temp_img.array = (image.array - mid) * factor + mid
    return temp_img


def get_neighbors_total(x, y, c, kernel_size, image):
    # number of cells to consider on each side of the current cell
    neighbor_range = kernel_size // 2
    rows, cols = image.array.shape[0], image.array.shape[1]
    total = 0
    for x_i in range(x - neighbor_range, x + neighbor_range + 1):
        for y_i in range(y - neighbor_range, y + neighbor_range + 1):
            if (x_i < 0 or y_i < 0 or x_i >= rows or y_i >= cols):
                continue
            total += image.array[x_i, y_i, c]
    return total


def blur(image, kernel_size):
    # kernel size is the number of pixels to take into account when applying the blur
    # (ie kernel_size = 3 would be neighbors to the left/right, top/bottom, and diagonals)
    # kernel size should always be an *odd* number
    x_pixels, y_pixels, channels = image.array.shape
    temp_img = Image(x_pixels, y_pixels, channels)

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(channels):
                # naive implementation
                total = get_neighbors_total(x, y, c, kernel_size, image)
                temp_img.array[x, y, c] = total / (kernel_size**2)
    return temp_img


if __name__ == "__main__":
    lake = Image(filename="lake.png")
    city = Image(filename="city.png")

    img_brighten = adjust_brightness(lake, 1.8)
    img_darken = adjust_brightness(city, 0.3)
    img_brighten.write("img_brighten.png")
    img_darken.write("img_darken.png")

    img_inc_contrast = adjust_contrast(lake, 2, 0.5)
    img_dec_contrast = adjust_contrast(city, 0.5, 0.5)
    img_inc_contrast.write("img_inc_contrast.png")
    img_dec_contrast.write("img_dec_contrast.png")

    img_blur3 = blur(city, 3)
    img_blur7 = blur(city, 7)
    img_blur3.write("img_blur_3.png")
    img_blur7.write("img_blur_7.png")