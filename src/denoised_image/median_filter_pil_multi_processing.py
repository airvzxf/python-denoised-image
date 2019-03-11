#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
De-noising an image.

This version is the median filter code which use Pillow for handle the images but the improvement was that
the script runs multi-process to does all the images at the same time also for fill the new images there two options
one with multi-threading and other without it.

Note:
    Using multi-threading with a lot of files is causing crashes also it's slower than run without multi-threading.
"""
from functools import reduce
from multiprocessing import Process
from threading import Thread

from PIL import Image


def create_chunks(flat_list: list, n: int) -> list:
    """
    Create a bi-dimensional list given a flat list and the number for chunks it.

    :param flat_list: list
    :param flat_list: The flat list.

    :param n: int
    :param n: The number of limit or the number to chunk it.

    :rtype: list
    """
    for i in range(0, len(flat_list), n):
        yield flat_list[i:i + n]


def set_new_pixel(image: list, new_pixels_array: list, i: int, j: int) -> None:
    """
    Set the median pixel which works sorting the neighbors and taking the middle of those.

    :rtype image: list
    :param image: The original image converted in a bi-dimensional list of pixels as tuples.

    :rtype new_pixels_array: list
    :param new_pixels_array: The new image which needs to put the new median pixel.

    :rtype i: int
    :param i: The used row position.

    :rtype j: int
    :param j: The used column position

    :rtype: None
    :return: The list converted in 2D array with columns as width and rows as height.
    """
    neighborhood = [(0, 0)] * 9

    try:
        neighborhood[0] = image[i - 1][j - 1]
        neighborhood[1] = image[i - 1][j]
        neighborhood[2] = image[i - 1][j + 1]
        neighborhood[3] = image[i][j - 1]
        neighborhood[4] = image[i][j]
        neighborhood[5] = image[i][j + 1]
        neighborhood[6] = image[i + 1][j - 1]
        neighborhood[7] = image[i + 1][j]
        neighborhood[8] = image[i + 1][j + 1]
    except IndexError:
        new_pixels_array[i][j] = image[i][j]
        return

    neighborhood.sort()
    new_pixels_array[i][j] = neighborhood[4]


def get_denoised_image(pixels_array: list, columns: int = 0, rows: int = 0, multi_threaded: bool = True) -> Image.Image:
    """
    De-noise an image get all the neighbors around and then sort and take the middle value.

    :rtype pixels_array: list
    :param pixels_array: The original image converted into a bi-dimensional array which every pixel.

    :rtype columns: int
    :param columns: Total of columns or in other words the width of the image.

    :rtype rows: int
    :param rows: Total of rows or in other words the height of the image.

    :rtype multi_threaded: bool
    :param multi_threaded: Run multi-threading for set the new pixels.

    :rtype: Image.Image
    :return: The new image with the median filtered pixels.
    """
    new_image = Image.new('RGB', (columns, rows), 'white')
    new_pixels_array = []
    threads = []

    for i in range(0, rows):
        new_pixels_array.append([])

        for j in range(0, columns):
            new_pixels_array[i].append([])

            if multi_threaded:
                try:
                    threads.append(
                        Thread(
                            target=set_new_pixel, args=(pixels_array, new_pixels_array, i, j),
                            name='Thread #{%i}-{%i}' % (i, j)
                        )
                    )
                    threads[-1].start()
                except Exception as e:
                    print('*** Error: ', e)
                    exit(-1)
            else:
                set_new_pixel(pixels_array, new_pixels_array, i, j)

    if multi_threaded:
        for thread in threads:
            thread.join()
        print('Exiting Main Thread')

    new_pixels_flat_array = reduce(lambda x, y: x + y, new_pixels_array)
    new_image.putdata(new_pixels_flat_array)

    return new_image


def start_denoised_image(image_name: str, image_extension: str) -> None:
    """
    De-nose an image and start to de-noising the de-noised image a couple times, it's helpful when the image is cleaned
    after 3 or 10 times.

    :rtype image_name: str
    :param image_name: The image path and file name.

    :rtype image_extension: str
    :param image_extension: The image extension which includes the dot.

    :rtype: None
    """
    multi_threaded = False
    image_pillow = Image.open(image_name + image_extension)
    width, height = image_pillow.size
    pixels = list(create_chunks(list(image_pillow.getdata()), width))

    new_image_pillow = get_denoised_image(pixels, width, height, multi_threaded=multi_threaded)
    new_image_pillow.save(image_name + 'z_denoised_1' + image_extension, 'PNG')

    for index in range(1, 3):
        image_pillow = Image.open(image_name + 'z_denoised_' + str(index) + image_extension)
        width, height = image_pillow.size

        pixels = list(create_chunks(list(image_pillow.getdata()), width))
        new_image_pillow = get_denoised_image(pixels, width, height, multi_threaded=multi_threaded)
        new_image_pillow.save(image_name + 'z_denoised_' + str(index + 1) + image_extension, 'PNG')


def main() -> None:
    """
    The main method which run this script.

    :rtype: None
    """
    image_extension = '.png'
    processing = []
    images = [
        '../resources/cat',
        '../resources/mona_lisa',
        '../resources/noise-image',
        # '../resources/noise_1/b1',
        # '../resources/noise_1/b2',
        # '../resources/noise_1/d1',
        # '../resources/noise_1/f1',
        # '../resources/noise_1/f2',
        # '../resources/noise_1/f3',
        # '../resources/noise_2/b1',
        # '../resources/noise_2/b2',
        # '../resources/noise_2/d1',
        # '../resources/noise_2/f1',
        # '../resources/noise_2/f2',
        # '../resources/noise_2/f3',
        # '../resources/noise_3/b1',
        # '../resources/noise_3/b2',
        # '../resources/noise_3/d1',
        # '../resources/noise_3/f1',
        # '../resources/noise_3/f2',
        # '../resources/noise_3/f3',
        # '../resources/noise_4/b1',
        # '../resources/noise_4/b2',
        # '../resources/noise_4/d1',
        # '../resources/noise_4/f1',
        # '../resources/noise_4/f2',
        # '../resources/noise_4/f3',
    ]

    for image_name in images:
        processing.append(
            Process(
                target=start_denoised_image, args=(image_name, image_extension),
                name='Processing: {%s}{%s}' % (image_name, image_extension)
            )
        )
        processing[-1].start()

    for processor in processing:
        processor.join()
        print('Finished the processing')


if __name__ == "__main__":
    main()
