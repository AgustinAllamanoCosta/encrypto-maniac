#!/bin/bash 

HOST=192.168.0.90
SSH_PORT=22
SSH_USER=root
SSH_PRIVATE_KEY="E:\Espacio de trabajo\EncryptoManiac\Deploy\Web\id_rsa"

remote.execute() { 
    
    COMMAND=$@

    ( 
      set -x; 
      ssh -o StrictHostKeyChecking=no \
          -o UserKnownHostsFile=/dev/null \
          -o LogLevel=error \
          -p $SSH_PORT \
          -i $SSH_PRIVATE_KEY \
          $SSH_USER@$HOST \
          $COMMAND
   )
}

remote.copy() {                                                                                                                       

    FROM=$1
    TO=$2
    remote.execute mkdir -p $TO
    (
      set -x;<
      scp -o StrictHostKeyChecking=no \
          -o UserKnownHostsFile=/dev/null \
          -o LogLevel=error \
          -P $SSH_PORT \
          -i $SSH_PRIVATE_KEY \
          $FROM \
          $SSH_USER@$HOST:$TO
    )
}

_run(){ 
	remote.execute docker login ghcr.io -u agustinallamanoocosta -p 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
    remote.execute docker pull ghcr.io/agustinallamanocosta/encryptoManiac:latest 
    remote.execute docker stop em
    remote.execute docker run -d -t --rm --name encryptoM -p 80:5000 -v /etc/baseEncryoptoM:/EncryptadorManiac/Recursos -v /etc/baseEncryoptoMWeb:/EncryptadorManiac/Web/Recursos ghcr.io/agustinallamanocosta/encryptoManiac:latest
}