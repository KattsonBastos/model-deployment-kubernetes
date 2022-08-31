FROM python:3.8-slim

COPY ./main /main

COPY ./requirements.txt /requirements.txt

RUN mkdir root/.streamlit

COPY ./config.toml /root/.streamlit/config.toml
COPY ./credentials.toml /root/.streamlit/credentials.toml

RUN pip install -r requirements.txt

EXPOSE 80

WORKDIR /main

CMD ["sh", "-c", "streamlit run --server.port 80 app.py"]
