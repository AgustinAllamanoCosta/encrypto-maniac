cd $WORKSPACE
docker build -t ghcr.io/agustinallamanocosta/encryptoManiac:latest -f $1/Dockerfile .
docker push ghcr.io/agustinallamanocosta/encryptoManiac:latest