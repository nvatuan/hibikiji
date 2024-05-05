#!/bin/bash

IMAGE_TAG=nvat/redicheck:v0.1
# docker login

## If you are using Intel Mac, you can use the following command to build the image for AMD64 architecture
docker build -t $IMAGE_TAG . --no-cache=true --platform=linux/amd64

## If you are using M1 Mac, you can use the following command to build the image for ARM64 architecture
# docker build -t $IMAGE_TAG . --no-cache=true --platform=linux/arm64 

docker push $IMAGE_TAG
