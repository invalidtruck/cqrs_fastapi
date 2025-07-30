FROM python:3.12-slim-bookworm

RUN pip install --no-cache-dir --upgrade pip setuptools wheel
WORKDIR /app

COPY ./app /app/app
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
