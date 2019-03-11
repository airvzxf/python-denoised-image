# Python: Denoised image.



## The statement.

An image can be seen as bitmap or a matrix of pixels, a pretty common problem nowadays is that images could contain some
noise (invalid pixels),
so most of the modern pictures applications denoised the image or make it smoother.

Your objective is to create an application that applies the denoised.



### Restrictions.

- No OpenCV usage

- No Numpy/ third party libraries to apply filters.



### What you could use?

- A library that is only part of the standard library of your preferred programming language to load the picture into
memory.



### What would be evaluated?

- Your creativity using data structures, optimization steps to play with the image.

- Your algorithms implementation and justification to decide which one to pick.



## Usage

Run every single script to denoised the image, you're able to uncomment or add images in the source to do
your own examples.

```bash
#!/usr/bin/env bash

BASE_DIR=$(pwd)
cd ${BASE_DIR}/src/denoised_image

# Run the base script with median filter.
${BASE_DIR}/src/venv/bin/python ${BASE_DIR}/src/denoised_image/median_filter_pil.py

# Run mine variation of the median filter script.
${BASE_DIR}/src/venv/bin/python ${BASE_DIR}/src/denoised_image/median_filter_pil_mine.py

# Run mine base script using multi-processor also doing denoised for a lot of images.
${BASE_DIR}/src/venv/bin/python ${BASE_DIR}/src/denoised_image/median_filter_pil_multi_processing.py

# Delete generated files
#rm -fR *z_*
```

The script `median_filter_without_libraries.py` was my first try to extract the image pixel from the binary file with
any libraries.



## Docker usage:

It's quite easy as run `./src/run.sh` then it builds and runs docker also it executes the
`median_filter_pil_multi_processing.py` script and copies the denoised images from the container to the local machine.

In the `./src/run.sh` script there's some variable `IMAGES_DIR` which needs to change the value to your valid local
path.

The repository is able to download from:

`docker pull airvzxf/python_denoised_image_with_median_filter_docker_image`



## Scripts:

- [median_filter_without_libraries.py](./src/denoised_image/median_filter_without_libraries.py)
- [median_filter_pil.py](./src/denoised_image/median_filter_pil.py)
- [median_filter_pil_mine.py](./src/denoised_image/median_filter_pil_mine.py)
- [median_filter_pil_multi_processing.py](./src/denoised_image/median_filter_pil_multi_processing.py)



## References:

Median filter:<br>
- https://en.wikipedia.org/wiki/Median_filter
- https://homepages.inf.ed.ac.uk/rbf/HIPR2/median.htm

Patch-based Image De-noising:<br>
- The image example in this web page is the same as the resource image
[noise-image.png](./src/resources/noise-image.png) and [denoised-image.png](./src/resources/denoised-image.png).
- https://www.irisa.fr/vista/Themes/Demos/Debruitage/ImageDenoising.html

Examples with code:
- [How to build amazing image filters with Python:
Median filter and Sobel filter](https://medium.com/@enzoftware/22aeb8e2f540)
- [simple example how median filter works](http://artemhlezin.com/2016/09/04/median.html)

Image de-noising algorithms:<br>
- Slide #17, it shows examples between filters and their the differences.
- https://es.slideshare.net/mohammadsunny92/image-denoising-algorithms

A review of image de-noising algorithms, whit a new one.<br>
- "There are many versions of AFh (Anisotropic filters), all yielding an asymptotic estimate equivalent
to the one in Theorem 2.3 (Total variation): the famous median filter [14], an inf-sup filter on segments
centered at x [5], and the clever numerical implementation of the mean curvature
equation in [21]. So all of those filters have in common the good preservation of edges,
but they perform poorly on flat regions and are worse there than a Gaussian blur."
- https://projects.iq.harvard.edu/files/imagenesmedicas/files/buades-coll-etal2005.pdf

Patch-based models and algorithms for image de-noising.<br>
- https://jivp-eurasipjournals.springeropen.com/articles/10.1186/s13640-017-0203-4
