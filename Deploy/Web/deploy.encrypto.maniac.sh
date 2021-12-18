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

_run(){ 
	
}