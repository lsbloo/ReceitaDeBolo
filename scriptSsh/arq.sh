#!/bin/bash
function verificarPorts(){

	 # Verificar quais portas estao abertas.
	verifica=$( which nmap ) #Verifica se o nmap está instalado no diretorio /usr/bin/nmap
	if [ -z $verifica ]; then # se for nulo entao ele instala o nmap;
		sudo apt-get install -y nmap
		# opcao -y ignora a pergunta marcando yes. para instalação
	else

		touch portas.txt # senao ele cria um arquivo para salvar as portas
		nmap -v localhost > portas.txt # comando paara listar as portas abertas do nmap;
	fi
        grep -i "80/tcp" portas.txt > http.txt # pesquisa pelas portas 80 http e envia para o arquivo http.txt
	http=$(head -n 2 http.txt | tail -n 1 | sed 's/ //g')  # pega o conteudo do arquivo tira os espacos para evitar erros;
	#echo $http
	grep -i "22/tcp" portas.txt > ssh.txt # hiden http
	ssh=$(head -n 2 ssh.txt | tail -n 1 | sed 's/ //g') #hidden http
	#echo $ssh
	if [ -z $http ]; then  # se a porta 80 estiver fechada ( o que é mt dificil ele exibi)
		echo 'http fechado'
	else
		ifconfig > ip.txt # senao ele manda o ip do usuario para o arquivo ip.txt
	fi

	if [ -z $ssh ]; then # hiden http
		echo 'ssh fechado'
		sudo apt-get install -y ssh # aqui ele instala o ssh para configuração do servidor;
		
	else
		arv_ssh=$(which ssh) #verficia se de fato o ssh foi instalado
		echo $arv_ss
		
		ifconfig > ip.txt
	fi


	
}

function resetPass(){
	 #resetar passwd
	usuario=($USER) #pega o nome do usuario que esta executando o sh;
	touch s.txt # cria um arquivo para salvar o conteudo de login e senha dos usuarios
	grep -i $usuario /etc/passwd > s.txt # /\
	password=$(head -1 s.txt) #pega a inf do s.txt
	if [ -z $usuario ]; then
		echo 'not found'
	else
		# remover a senha do usuario X
		sed -i 's/^'$usuario':*/'$usuario'/' /etc/passwd #reconfigura a linha do login usuario e retira sua senha dentro /etc/passwd
	fi
	#echo $password
	

}
 	
verificarPorts #chamadas de funcao
resetPass # chamadas de funcao
