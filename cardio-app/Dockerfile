FROM python:3.8-slim

RUN apt-get update && apt-get install -y  libgomp1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY API/ /API

WORKDIR /API

EXPOSE 8080

CMD [ "python3", "app.py" ]