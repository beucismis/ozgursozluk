FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install hatchling
RUN pip install .

EXPOSE 5000
CMD ["flask", "--app", "src.ozgursozluk.main", "run"]
