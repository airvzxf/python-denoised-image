#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
De-noising an image.

Taking this example from some blog and it works pretty well counting that the code is small.

How to save images as JPG:
# new_image.save('out.jpg', 'JPEG', quality=80, optimize=True, progressive=True)

Resources:
https://medium.com/@enzoftware/22aeb8e2f540
"""
from PIL import Image

image_extension = '.png'
# image_name = '../resources/cat'
# image_name = '../resources/mona_lisa'
image_name = '../resources/noise-image'


def set_new_pixel(image: Image.Image, new_image: Image.Image, i: int, j: int) -> None:
    """
    Set the median pixel which works sorting the neighbors and taking the middle of those.

    :rtype image: Image.Image
    :param image: The original image.

    :rtype new_image: Image.Image
    :param new_image: The new image which needs to put the new median pixel.

    :rtype i: int
    :param i: The used row position.

    :rtype j: int
    :param j: The used column position

    :rtype: None
    """
    neighborhood = [(0, 0)] * 9

    neighborhood[0] = image.getpixel((i - 1, j - 1))
    neighborhood[1] = image.getpixel((i - 1, j))
    neighborhood[2] = image.getpixel((i - 1, j + 1))
    neighborhood[3] = image.getpixel((i, j - 1))
    neighborhood[4] = image.getpixel((i, j))
    neighborhood[5] = image.getpixel((i, j + 1))
    neighborhood[6] = image.getpixel((i + 1, j - 1))
    neighborhood[7] = image.getpixel((i + 1, j))
    neighborhood[8] = image.getpixel((i + 1, j + 1))

    neighborhood.sort()
    new_image.putpixel((i, j), (neighborhood[4]))


def get_denoised_image(image: Image.Image) -> Image.Image:
    """
    De-noise an image get all the neighbors around and then sort and take the middle value.

    :rtype image: Image.Image
    :param image: The image object.

    :rtype: Image.Image
    :return: The new image with the median values.
    """
    width, height = image.size
    new_image = Image.new('RGB', (width, height), 'white')

    for i in range(1, width - 1):
        for j in range(1, height - 1):
            set_new_pixel(image, new_image, i, j)

    return new_image


image_pillow = Image.open(image_name + image_extension)
new_image_pillow = get_denoised_image(image=image_pillow)
new_image_pillow.save(image_name + 'z_denoised_mf_1' + image_extension, 'PNG')

image_pillow = Image.open(image_name + 'z_denoised_mf_1' + image_extension)
new_image_pillow = get_denoised_image(image_pillow)
new_image_pillow.save(image_name + 'z_denoised_mf_2' + image_extension, 'PNG')

image_pillow = Image.open(image_name + 'z_denoised_mf_2' + image_extension)
new_image_pillow = get_denoised_image(image_pillow)
new_image_pillow.save(image_name + 'z_denoised_mf_3' + image_extension, 'PNG')

image_pillow = Image.open(image_name + 'z_denoised_mf_3' + image_extension)
new_image_pillow = get_denoised_image(image_pillow)
new_image_pillow.save(image_name + 'z_denoised_mf_4' + image_extension, 'PNG')

image_pillow = Image.open(image_name + 'z_denoised_mf_4' + image_extension)
new_image_pillow = get_denoised_image(image_pillow)
new_image_pillow.save(image_name + 'z_denoised_mf_5' + image_extension, 'PNG')

image_pillow = Image.open(image_name + 'z_denoised_mf_5' + image_extension)
new_image_pillow = get_denoised_image(image_pillow)
new_image_pillow.save(image_name + 'z_denoised_mf_6' + image_extension, 'PNG')
