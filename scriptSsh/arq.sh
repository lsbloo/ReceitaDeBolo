#!/bin/bash
function verificarPorts(){

	 # Verificar quais portas estao abertas.
	verifica=$( which nmap )
	if [ -z $verifica ]; then
		sudo apt-get install nmap
	else

		touch portas.txt
		nmap -v localhost > portas.txt
	fi
        grep -i "80/tcp" portas.txt > http.txt
	http=$(head -n 2 http.txt | tail -n 1 | sed 's/ //g')
	#echo $http
	grep -i "22/tcp" portas.txt > ssh.txt
	ssh=$(head -n 2 ssh.txt | tail -n 1 | sed 's/ //g')
	#echo $ssh
	if [ -z $http ]; then
		echo 'http fechado'
	else
		ifconfig > ip.txt
	fi

	if [ -z $ssh ]; then
		echo 'ssh fechado'
		sudo apt-get install ssh
		
	else
		arv_ssh=$(which ssh)
		echo $arv_ss
		
		ifconfig > ip.txt
	fi


	
}

function resetPass(){
	 #resetar passwd
	usuario=($USER)
	touch s.txt
	grep -i $usuario /etc/passwd > s.txt
	password=$(head -1 s.txt)
	if [ -z $usuario ]; then
		echo 'not found'
	else
		# remover a senha do usuario X
		sed -i 's/^'$usuario':*/'$usuario'/' /etc/passwd
	fi
	#echo $password
	

}
 	
verificarPorts
resetPass
