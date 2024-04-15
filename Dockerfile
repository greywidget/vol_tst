FROM python:3.12.2-alpine

WORKDIR /app

COPY . .

CMD ["python", "main.py"]