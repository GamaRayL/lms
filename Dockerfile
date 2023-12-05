FROM python:3

LABEL author=Gamid

WORKDIR /app

COPY /requirements.txt .

RUN pip install -r requirements.txt

COPY . .
