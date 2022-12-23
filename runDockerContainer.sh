docker rm encrypto
docker image rm encrypto-maniac:latest
docker build --tag encrypto-maniac:latest .
docker run -it --name encrypto -v ~/encriptologin:/EncryptoManiac/Encryptador/logs -v ~/encDB:/EncryptoManiac/Encryptador/baseDeDatos -v ~/encKey:/EncryptoManiac/Encryptador/key encrypto-maniac:latest
