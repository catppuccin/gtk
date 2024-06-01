#!/bin/sh

# Default value for custom_version
VERSION="no"

while getopts v:h opt 2>/dev/null; do
  case "$opt" in
    v)
      VERSION=$OPTARG
      ;;
    h)
      echo "\
Usage: $0 [-v <version>]

Push script for Catppuccin's GTK docker build image

-v  Custom version to build the image (<your-image-name>:<version>)
    If you only want to generate the image with tag 'latest' use '-v no'
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

# Resolve the absolute path of the script without readlink
SCRIPT_PATH="$0"

# Check if SCRIPT_PATH is a symbolic link
while [ -h "$SCRIPT_PATH" ]; do
  LS=$(ls -ld "$SCRIPT_PATH")
  LINK=$(expr "$LS" : '.*-> \(.*\)$')
  if expr "$LINK" : '/.*' > /dev/null; then
    SCRIPT_PATH="$LINK"
  else
    SCRIPT_PATH=$(dirname "$SCRIPT_PATH")/"$LINK"
  fi
done

# Ensure we have an absolute path
case "$SCRIPT_PATH" in
  /*) ;;
  *) SCRIPT_PATH="$(pwd)/$SCRIPT_PATH" ;;
esac

# Path to script' dir
SCRIPT_DIR=$(cd "$(dirname "$SCRIPT_PATH")" && pwd)

# Path to the Dockerfile
DOCKERFILE_PATH="$SCRIPT_DIR/Dockerfile"

# Docker variables
IMAGE_NAME="ghcr.io/catppuccin/gtk"

# Detect podman
if command -v podman > /dev/null 2>&1; then
  CONTAINER_TOOL="podman"
elif command -v docker > /dev/null 2>&1; then
  CONTAINER_TOOL="docker"
else
  echo "Error: Neither podman nor docker is installed."
  exit 1
fi

# Clean previous generated images
$CONTAINER_TOOL image rm "$IMAGE_NAME:latest" 2> /dev/null
$CONTAINER_TOOL image rm "$IMAGE_NAME:$VERSION" 2> /dev/null

# Build the Docker image with latest tag
$CONTAINER_TOOL build -t "$IMAGE_NAME:latest" -f "$DOCKERFILE_PATH" "$SCRIPT_DIR/.."

# Execute docker tag command if VERSION is not "no"
if [ "$VERSION" != "no" ]; then
  $CONTAINER_TOOL tag "$IMAGE_NAME:latest" "$IMAGE_NAME:$VERSION"
fi
