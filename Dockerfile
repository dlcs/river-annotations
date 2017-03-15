FROM ubuntu

RUN apt-get -y update && apt-get install -y python-pip python-dev build-essential nginx uwsgi
RUN mkdir /opt/river

COPY *.py /opt/river/
COPY requirements.txt /opt/river/.
COPY river.ini /opt/river/.
COPY run_river_annotations.sh /opt/river/.

COPY etc/river.nginx.conf /etc/nginx/sites-available/river
RUN ln -s /etc/nginx/sites-available/river /etc/nginx/sites-enabled/river && rm -f /etc/nginx/sites-enabled/default

WORKDIR /opt/river

RUN pip install -r requirements.txt

CMD ./run_river_annotations.sh

EXPOSE 80
