FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY . .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir hatchling && \
    pip install --no-cache-dir .

EXPOSE 5000

CMD ["gunicorn", "src.ozgursozluk.main:app", "-b", "0.0.0.0:5000", "-w", "5"]
