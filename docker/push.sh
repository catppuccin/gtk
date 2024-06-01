#!/bin/sh

# Default value for parameters
VERSION="no"
USERNAME="no"
PASSWORD="no"

while getopts u:p:v:h opt 2>/dev/null; do
  case "$opt" in
    v)
      VERSION=$OPTARG
      ;;
    u)
      USERNAME=$OPTARG
      ;;
    p)
      PASSWORD=$OPTARG
      ;;
    h)
      echo "\
Usage: $0 [-v <version> | -u [your-github-username] | -p [your-github-password]]

Push script for Catppuccin's GTK docker build image

-v  Custom version to push the image (<your-image-name>:<version>)
-u  Your GitHub username that will be used to log into GHCR
-p  Your GitHub password that will be used to log into GHCR
-h  Print this help text" >&2
      exit 0
      ;;
    ?)
      echo "Usage: $0 [-h]" >&2
      exit 1
      ;;
  esac
done
if [ $# -eq 0 ]
  then
    echo "Usage: $0 [-h]"
    exit 1
fi


# Detect podman
if command -v podman > /dev/null 2>&1; then
  CONTAINER_TOOL="podman"
elif command -v docker > /dev/null 2>&1; then
  CONTAINER_TOOL="docker"
else
  echo "Error: Neither podman nor docker is installed."
  exit 1
fi

# Docker variables
IMAGE_NAME="ghcr.io/catppuccin/gtk"

# Log into ghcr
$CONTAINER_TOOL login ghcr.io -u $USERNAME --password $PASSWORD

# Push docker image with latest tag
$CONTAINER_TOOL push "$IMAGE_NAME:latest"

# Execute docker push for specific version if VERSION is not "no"
if [ "$VERSION" != "no" ]; then
  $CONTAINER_TOOL push "$IMAGE_NAME:$VERSION"
fi
