#!/bin/bash

# qsub needs Python 2 on the avakas cluster
N_JOBS=$(eval python prepare.py --count)
INDICES="0-${N_JOBS}"

export PYENV_VERSION=2.7.12

# you can specify the indices directly using:
# ./run_array.sh 3;4-6
if (( "$#" > 1 ))
then
  INDICES=$1;
fi

CMD="qsub -t ${INDICES} job_array.pbs"
echo $CMD
eval $CMD

unset PYENV_VERSION
