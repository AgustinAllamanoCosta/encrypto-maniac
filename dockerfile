FROM python:3.10.6
WORKDIR /EncryptoManiac
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "run.py"]