FROM python:3.8-alpine
RUN pip install ozgursozluk
EXPOSE 80
CMD python3 -m gunicorn ozgursozluk:app -b 0.0.0.0:80 -w 3
