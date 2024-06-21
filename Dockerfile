FROM python:3.8-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD python -m gunicorn ozgursozluk:app -b 0.0.0.0:8000 -w 3
