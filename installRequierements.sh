echo "Actualizando las dependencias"
sudo apt-get update
echo "Instalando paquetes del X11"
sudo apt-get install -y xclip xsel x11-xserver-utils 
echo "Instalando dependencias en requirements"
sudo pip3 install -r requirements.txt
echo "Dependencias intaladas"