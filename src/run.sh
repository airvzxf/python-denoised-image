#!/usr/bin/env bash

set -xve

IMAGE=python_denoised_image_with_median_filter__image
CONTAINER=python_denoised_image_with_median_filter__container
NEW_DIR=~/Downloads/denoised_images

docker build -t ${IMAGE} .
docker run -d --name ${CONTAINER} -it ${IMAGE} /bin/sh -c 'python3'



# Login into the container with bash
# docker exec -it ${CONTAINER} bash

# Execute the median filter script into the container
docker exec -it ${CONTAINER} /bin/sh -c 'ls -lha && echo -e "\n\n\n"'
#docker exec -it ${CONTAINER} /bin/sh -c 'cd denoised_image && ../venv/bin/python median_filter_pil.py'
#docker exec -it ${CONTAINER} /bin/sh -c 'cd denoised_image && ../venv/bin/python median_filter_pil_mine.py'
docker exec -it ${CONTAINER} /bin/sh -c 'cd denoised_image && ../venv/bin/python median_filter_pil_multi_processing.py'



# Get the images generated from the container to the local directory.
rm -fR ${NEW_DIR}
mkdir -p ${NEW_DIR}
docker cp ${CONTAINER}:/usr/src/app/resources ${NEW_DIR}

# Delete the directory and get the images again fix the bug about copy the resources folder and copy only the images.
rm -fR ${NEW_DIR}
docker cp ${CONTAINER}:/usr/src/app/resources ${NEW_DIR}
