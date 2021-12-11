FROM python:3 

WORKDIR /EncriptoManiac/

RUN pip install Flask

ENV FLASK_ENV="development"
ENV  FLASK_APP="E:/Espacio de trabajo/EncryptoManiac/Web/EncriptoWeb:crearAplicacion()"

COPY Encryptador .
COPY Recursos .
COPY Util .
COPY Web .
COPY __init__.py .

CMD [ "bash" ]