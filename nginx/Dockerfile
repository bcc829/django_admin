FROM nginx:1.17.4-alpine

COPY ./static /home/staticfiles/

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d
