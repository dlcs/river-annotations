#!/bin/bash

touch river_annotations_service.log

# python river_annotations.py &

# tail -f river_annotations_service.log

service nginx restart

cd /opt/river && uwsgi --ini /opt/river/river.ini

