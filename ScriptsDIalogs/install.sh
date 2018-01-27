#!/bin/bash



update(){
	sudo apt-get upgrade && sudo apt-get update
}
nanoRep(){
	nano  /etc/apt/sources.list
}
installProg(){
	nomeProg=$( dialog --stdout --inputbox 'Digite o nome do programa: ' 0 0 )
	
	if [ -z $nomeProg ]; then
		while [ -z $nomeProg ]; do
			nomeProg=$( dialog --stdout --inputbox 'Digite o nome do programa: ' 0 0 )
		done
	else
		sudo apt-get install $nomeProg
	fi
}
aptitude(){
	#sudo apt-get install aptitude
	sleep 2
	#Bugado kkk
	aptitude
}
confDpkg(){
	dpkg --reconfigure -a
}
distro=$( uname -n )
acessar=$( dialog --stdout --menu "InstaladorUbuntuv01" 30 50 20 update 'Update' alterarRep 'Alterar repositorios' instalar 'Instalar programa especificado' dpkg 'Corrigir erros do Dpkg' aptitude 'Utilizar o aptitude ?' )


case $acessar in

update)
	
	( echo 40 ; sleep 1 
	  echo 75 ; sleep 1 
          echo 100; sleep 1 ) | dialog --title 'Atualizando..' --gauge 'Atualizacao em: '$distro 8 40 60

	sleep 2
	update
	;;
alterarRep)
	
	nanoRep
	;;

instalar)
	installProg
	;;

aptitude)
	aptitude
	;;
dpkg)
	confDpkg
	;;
esac
