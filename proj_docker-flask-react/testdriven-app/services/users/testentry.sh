#!/bin/sh

set -e

echo "${0}: running tests"
python manage.py test
