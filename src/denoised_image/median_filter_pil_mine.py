#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
De-noising an image.

I took the median filter example which uses Pillow and I implemented get the median pixels and add it as the
median pixel instead of take the pixel on the position number four.

Note:
    Add the end in color images it changes the color also it doesn't improved the correction for the image.
"""

from PIL import Image

image_extension = '.png'
# image_name = '../resources/cat'
# image_name = '../resources/mona_lisa'
image_name = '../resources/noise-image'


def get_max_tuples(tuples: list) -> tuple:
    """
    Get the maximum value which is repeated tuple in this list of tuples.

    :rtype tuples: list
    :param tuples: List of tuples with the pixels values.

    :rtype: tuple
    :return: Return the maximum repeated tuple which represents a pixel.
    """
    unique_tuples = []
    repetitions = []

    for row in tuples:
        if row in unique_tuples:
            index = unique_tuples.index(row)
            repetitions[index] += 1
        else:
            unique_tuples.append(row)
            repetitions.append(1)

    max_repetitions = max(repetitions)

    index = 0
    tuples_median = [0, 0, 0, 0]
    values_median = 0
    for repetition in repetitions.copy():
        if repetition != max_repetitions:
            tuples_median[0] += unique_tuples[index][0]
            tuples_median[1] += unique_tuples[index][1]
            tuples_median[2] += unique_tuples[index][2]
            values_median += 1

            repetitions.pop(index)
            unique_tuples.pop(index)
            index -= 1
        index += 1

    if len(unique_tuples) > 1:
        if values_median > 0:
            tuples_median[0] = int(tuples_median[0] / values_median)
            tuples_median[1] = int(tuples_median[1] / values_median)
            tuples_median[2] = int(tuples_median[2] / values_median)

            median_distance = tuples_median[0] + tuples_median[1] + tuples_median[2]
        else:
            index = int(len(unique_tuples) / 2)
            median_distance = unique_tuples[index][0] + unique_tuples[index][1] + unique_tuples[index][2]

        last_distance = 0

        last_row = None
        for row in unique_tuples.copy():
            distance = row[0] + row[1] + row[2]
            the_distance = abs(median_distance - distance)

            if last_row is not None and last_row in unique_tuples:
                if the_distance < last_distance:
                    index = unique_tuples.index(last_row)
                    unique_tuples.pop(index)
                else:
                    index = unique_tuples.index(row)
                    unique_tuples.pop(index)

            last_row = row
            last_distance = the_distance

        pass

    return unique_tuples[0]


def get_denoised_image(image: Image.Image) -> Image.Image:
    """
    De-noise an image get all the neighbors around and then sort and take the middle value.

    :rtype image: Image.Image
    :param image: The image object.

    :rtype: Image.Image
    :return: The new image with the median values.
    """
    width, height = image.size
    neighborhood = [(0, 0)] * 9
    new_image = Image.new('RGB', (width, height), 'white')

    for i in range(1, width - 1):
        for j in range(1, height - 1):
            neighborhood[0] = image_pillow.getpixel((i - 1, j - 1))
            neighborhood[1] = image_pillow.getpixel((i - 1, j))
            neighborhood[2] = image_pillow.getpixel((i - 1, j + 1))
            neighborhood[3] = image_pillow.getpixel((i, j - 1))
            neighborhood[4] = image_pillow.getpixel((i, j))
            neighborhood[5] = image_pillow.getpixel((i, j + 1))
            neighborhood[6] = image_pillow.getpixel((i + 1, j - 1))
            neighborhood[7] = image_pillow.getpixel((i + 1, j))
            neighborhood[8] = image_pillow.getpixel((i + 1, j + 1))
            neighborhood.sort()

            new_pixel = get_max_tuples(neighborhood)
            new_image.putpixel((i, j), new_pixel)

    return new_image


image_pillow = Image.open(image_name + image_extension)
new_image_pillow = get_denoised_image(image_pillow)
new_image_pillow.save(image_name + 'z_denoised_mine_1' + image_extension, 'PNG')

image_pillow = Image.open(image_name + 'z_denoised_mine_1' + image_extension)
new_image_pillow = get_denoised_image(image_pillow)
new_image_pillow.save(image_name + 'z_denoised_mine_2' + image_extension, 'PNG')

image_pillow = Image.open(image_name + 'z_denoised_mine_2' + image_extension)
new_image_pillow = get_denoised_image(image_pillow)
new_image_pillow.save(image_name + 'z_denoised_mine_3' + image_extension, 'PNG')

image_pillow = Image.open(image_name + 'z_denoised_mine_3' + image_extension)
new_image_pillow = get_denoised_image(image_pillow)
new_image_pillow.save(image_name + 'z_denoised_mine_4' + image_extension, 'PNG')

image_pillow = Image.open(image_name + 'z_denoised_mine_4' + image_extension)
new_image_pillow = get_denoised_image(image_pillow)
new_image_pillow.save(image_name + 'z_denoised_mine_5' + image_extension, 'PNG')

image_pillow = Image.open(image_name + 'z_denoised_mine_5' + image_extension)
new_image_pillow = get_denoised_image(image_pillow)
new_image_pillow.save(image_name + 'z_denoised_mine_6' + image_extension, 'PNG')
