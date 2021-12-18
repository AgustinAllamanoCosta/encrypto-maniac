cd $WORKSPACE
docker build -t ghcr.io/agustinallamanocosta/encrypto-maniac:latest -f $1/Dockerfile .
docker login ghcr.io -u allamanocostaagustin@gmail.com -p $2
docker push ghcr.io/agustinallamanocosta/encrypto-maniac:latest