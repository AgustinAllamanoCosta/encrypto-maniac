FROM python:3 

WORKDIR /EncryptoManiac/

RUN python -m pip install --upgrade pip && \
    	      pip install cryptography  && \
	      	  pip install Flask 

ENV FLASK_ENV="development"
ENV FLASK_APP="/EncryptoManiac/Web/EncriptoWeb:crearAplicacion()"
ENV PYTHONPATH="/EncryptoManiac/"

RUN mkdir /EncryptoManiac/ && mkdir /EncryptoManiac/Web/Recursos

COPY . .

CMD [ "bash" ]
