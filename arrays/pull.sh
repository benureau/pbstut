#!/bin/bash
SRC=$(eval python prepare.py --path)
DEST=${2-"code"}

# push code to the cluster
rsync -azv avakas:${SRC} ~/research/data/${SRC}/
