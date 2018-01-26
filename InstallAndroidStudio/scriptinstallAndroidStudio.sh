#!/bin/bash

#Script com funcao de instalar o android studio via ppa.

exeAndroid(){
	#Funcao de instalacao do android Studio

	sudo add-apt-repository ppa:ubuntu-desktop/ubuntu-make -y && sudo apt-get update && sudo apt-get install ubuntu-make -y
	
	sleep 2
	
	umake android

	echo 'INSTALADO....100%'
}
unistallAndroid(){
	umake android --remove
	echo 'Desinstalado!'

}
echo 'Digite [1] se deseja instalar o androidStudio ou [2] se deseja remover'
echo
read opcao

if [ $opcao -eq 1 ]; then
	exeAndroid

elif [ $opcao -eq 2 ]; then
	unistallAndroid

else
	echo 'Fim'
fi

