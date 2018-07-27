#!/usr/bin/env bash

sass home/static/sass/global.scss ../static/css/global.css

python manage.py runserver