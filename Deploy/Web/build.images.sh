cd $WORKSPACE
docker build -t ghcr.io/agustinallamanocosta/encrypto-maniac:latest -f $1/Dockerfile .
docker push ghcr.io/agustinallamanocosta/encrypto-maniac:latest