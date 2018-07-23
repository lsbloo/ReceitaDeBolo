#!/bin/bash
#Objetivo? - verificar portas do meu aplicativo APP4SOCIETY que estão sendo utilizadas;

portweb=":8080 "
portpostgrel=":5432"
portpostgreaux=":5444"
namesql="postegresql"
op='xd'
function verificWEB(){
	# estado de Escuta - ONLINE
	echo 'Porta da aplicacao Spring BOT '
	#echo $portweb
	echo ''
	saida=$(lsof -i $portweb | grep LISTEN)
	if [ -z $saida ]; then
		echo 'Aplicação SpringBOT OFFLINE'
		echo ''
	else
		echo 'Aplicacao SpringBOT ONLINE'
		echo ''
	fi
}

function verificPostGree(){
	# Verifica se o PostGreeSQL foi iniciado com sucesso 
	# atualmente minha porta padrao está 5432

	echo 'Porta do postgreSQL '
	echo ''
	saida_post=$(lsof -i $portpostgrel | grep LISTEN)
	
	if [ -z $saida_post ]; then
		echo 'PostGREESQL Nao foi iniciado'
		echo ''
	else
		echo 'PostGreeSQL iniciado'
		echo ''
	fi

}
function recoverMyIP(){
	#Recupera o meu ip atual da maquina e exibe na tela
	recoveryIp=$(ifconfig)
	touch arq
	ifconfig > arq
	cat -n arq
}

while [ $op != 4 ]; do
	echo '[1]- verific SpringBOT, [2]-POSTGREESQL , [3]- YOUR IP -- [4] SAIR '
	read op
	if [ $op -eq 1 ]; then
		verificWEB
	elif [ $op -eq 2 ]; then
		verificPostGree
	elif [ $op -eq 3 ]; then
		recoverMyIP

	elif [ $op -eq 4 ]; then
		echo 'Saindo..'
	
	else
		echo 'Entrada invalida!'
	fi
done
