FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip3 install --no-cache -r requirements.txt

CMD ["python", "api-service.py"]