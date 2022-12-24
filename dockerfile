FROM python:3.10.6
WORKDIR /EncryptoManiac
ENV DISPLAY="127.0.0.1:0"
COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install -y xclip xsel x11-xserver-utils && pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "run.py"]