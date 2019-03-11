#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
De-noising an image.

I tried to extract the pixel from the binary file, and convert it into a RGBA value
but it was difficult and I consumed my timebox.

NOTE:
    Incomplete example, it needs:
    - Create methods for check the image format (JPG, PNG, etc.)
    - Create methods to extract the image bytes based on the image format.
    - Extract the pixels based on the bytes.
    - Get the size image (width x height) to create a matrix.
    - Convert pixel into a RGBA.
"""
image_extension = '.png'
image_name = '../resources/noise-image'
# denoised_image = open(image_name + 'z_denoised_1' + image_extension, 'wb')

with open(image_name + image_extension, 'rb') as image:
    for row_bytes in image:
        print(len(row_bytes), row_bytes)

    # denoised_image.write(row_bytes)

# denoised_image.close()
