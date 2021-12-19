FROM python:3 

WORKDIR /EncryptoManiac/

RUN python -m pip install --upgrade pip && \
    	      pip install cryptography  && \
	      	  pip install Flask 

ENV FLASK_ENV="development"
ENV FLASK_APP="/EncryptoManiac/Web/EncriptoWeb"
ENV PYTHONPATH="/EncryptoManiac/"

EXPOSE 5000

COPY  EncryptoManiac/Encryptador/ /EncryptoManiac/Encryptador/
RUN   mkdir /EncryptoManiac/Recursos/
COPY  EncryptoManiac/Util  /EncryptoManiac/Util
COPY  EncryptoManiac/Web  /EncryptoManiac/Web
RUN   mkdir /EncryptoManiac/Web/Recursos/
COPY  EncryptoManiac/run.flask.sh /EncryptoManiac
RUN chmod u+x /EncryptoManiac/run.flask.sh

CMD [ "./EncryptoManiac/run.flask.sh" ]
