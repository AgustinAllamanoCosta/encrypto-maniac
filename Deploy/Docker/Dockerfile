FROM python:3 

WORKDIR /EncryptoManiac/

RUN python -m pip install --upgrade pip && \
    	      pip install cryptography  && \
	      	  pip install Flask 

ENV FLASK_ENV="development"
ENV FLASK_APP="/EncryptoManiac/Web/EncriptoWeb:crearAplicacion()"
ENV PYTHONPATH="/EncryptoManiac/"

COPY  EncryptoManiac/Encryptador/ /EncryptoManiac/Encryptador/
RUN mkdir /EncryptoManiac/Recursos/
COPY  EncryptoManiac/Encryptador/Util  /EncryptoManiac/Encryptador/Util
COPY  EncryptoManiac/Encryptador/Web  /EncryptoManiac/Encryptador/Web
RUN mkdir /EncryptoManiac/Web/Recursos/

CMD [ "bash" ]
