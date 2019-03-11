#!/usr/bin/env bash

set -xve

IMAGE=python_denoised_image_with_median_filter_docker_image
CONTAINER=python_denoised_image_with_median_filter_docker_container

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
IMAGES_DIR=~/Downloads/denoised_images



docker build -t ${IMAGE} ${DIR}
docker run -d --name ${CONTAINER} -it ${IMAGE} /bin/sh -c 'python3'



# Login into the container with bash
# docker exec -it ${CONTAINER} bash

# Execute the median filter script into the container
docker exec -it ${CONTAINER} /bin/sh -c 'ls -lha && echo -e "\n\n\n"'
#docker exec -it ${CONTAINER} /bin/sh -c 'cd denoised_image && python median_filter_pil.py'
#docker exec -it ${CONTAINER} /bin/sh -c 'cd denoised_image && python median_filter_pil_mine.py'
docker exec -it ${CONTAINER} /bin/sh -c 'cd denoised_image && python median_filter_pil_multi_processing.py'



# Get the images generated from the container to the local directory.
rm -fR ${IMAGES_DIR}
docker cp ${CONTAINER}:/usr/src/app/resources ${IMAGES_DIR}
