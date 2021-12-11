FROM python:3 

WORKDIR /EncriptoManiac/

RUN python -m pip install --upgrade pip && \
    	      pip install cryptography  &&\
	      pip install Flask 

ENV FLASK_ENV="development"
ENV FLASK_APP="/EncryptoManiac/Web/EncriptoWeb:crearAplicacion()"
ENV PYTHONPATH="/EncryptoManiac"

COPY . .
RUN mkdir /EncryptadorManiac/Web/Recursos

CMD [ "bash" ]
