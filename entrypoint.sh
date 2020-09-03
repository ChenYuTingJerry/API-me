#!/bin/bash
rm -rf tmp
set -e

if [ "$ENV" = 'prod' ]
then
  eval $(aws-env)
fi

python run.py


