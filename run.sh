#!/bin/bash

DEPLOYMENT_FOLDER='/opt/example'

source $DEPLOYMENT_FOLDER/venv/bin/activate

gunicorn app:application \
         --bind 127.0.0.1:5000 \
         --workers 2 \
         --threads 2
