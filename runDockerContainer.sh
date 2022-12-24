docker rm encrypto
docker image rm encrypto-maniac:latest
docker build --tag encrypto-maniac:latest .
xhost +
docker run -it --name encrypto --net=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v ~/encriptologin:/EncryptoManiac/Encryptador/logs -v ~/encDB:/EncryptoManiac/Encryptador/baseDeDatos -v ~/encKey:/EncryptoManiac/Encryptador/key encrypto-maniac:latest
xhost -
