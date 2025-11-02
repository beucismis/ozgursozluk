FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY . .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir hatchling && \
    pip install --no-cache-dir .

EXPOSE 5000

ENV FLASK_APP=ozgursozluk.main:app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=1

CMD ["flask", "run"]
