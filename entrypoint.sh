#!/bin/bash
rm -rf tmp
set -e

if [ "$ENABLE_SSM" ]
then
  eval $(aws-env)
fi

python run.py


