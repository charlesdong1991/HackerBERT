FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -U pip
RUN pip install bert-serving-client==1.9.8 elasticsearch==7.0.4 Flask==1.1.1

CMD ["python", "app.py"]
