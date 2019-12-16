FROM python:3.7
MAINTAINER Jun-Young Jeong <abcdefssk1@gmail.com>

ADD . /usr/src/notice_admin

WORKDIR /usr/src/notice_admin

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD exec gunicorn notice_admin.wsgi:application --bind 0.0.0.0:8000 --workers 3

