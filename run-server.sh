#!/usr/bin/env bash

echo "******** Compiling sass ***********"

sass home/static/sass/global.scss home/static/css/global.css

echo "******** Starting server ***********"

python manage.py runserver