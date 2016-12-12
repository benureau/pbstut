#!/bin/bash
USERNAME="fbenurea"
SRC=${1-"."}
DEST=${2-"code"}

# push code to the cluster
rsync -azv avakas:/scratch/${USERNAME}/${SRC}/ ~/research/data/${SRC}/
