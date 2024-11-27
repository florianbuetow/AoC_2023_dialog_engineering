#!/bin/bash

# Define the image name
IMAGE_NAME="data-downloader-aoc23"

# Force rebuilding of the image to avoid caching issues
if [[ "$(docker images -q $IMAGE_NAME 2> /dev/null)" != "" ]]; then
  echo "Image $IMAGE_NAME already exists. Removing"
  docker rmi $IMAGE_NAME:latest
fi
echo "Building $IMAGE_NAME image..."
docker build --no-cache -f Dockerfile.data -t $IMAGE_NAME .

# Run the Docker container
echo "Running the Docker container to download daily input data for AoC 2023 ..."
docker run --rm -v "$(pwd)":/app/output $IMAGE_NAME

echo "Container execution finished."