FROM tensorflow/tensorflow:1.12.0-py3
RUN pip install -U pip
RUN pip install --no-cache-dir bert-serving-server
COPY ./ /app
COPY build-bert.sh /app
WORKDIR /app

ENTRYPOINT ["sh", "/app/build-bert.sh"]
