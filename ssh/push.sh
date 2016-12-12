#!/bin/bash

# usage:
# ./push.sh [source_directory] [destination_directory_on_avakas]

# default directories if none provided
SRC=${1-".."}
DEST=${2-"tutorial"}

# push code to the cluster
rsync -azv --delete \
      --exclude *.so \
      --exclude *.c \
      --exclude *.txt \
      --exclude *.npy \
      --exclude *.pyc \
      --exclude *.egg-info \
      --exclude *.trace \
      --exclude .git/ \
      --exclude data/ \
      --exclude __pycache__/ \
      $SRC avakas:$DEST/
