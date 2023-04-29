FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 80
CMD [ "python3", "-m", "gunicorn", "-b", "0.0.0.0:80"]
