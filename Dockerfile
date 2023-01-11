FROM ubuntu:22.04

RUN apt update && apt install -y python3 python3-pip libpq-dev

EXPOSE 8000

WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "uvicorn" ]
CMD [ "main:app", "--host=0.0.0.0", "--port=8000" ]