#!/bin/bash

# Objetivo SCRIPT: verifica pings em um determinado periodo de tempo
# se a media de pings for menor ou igual a 100 - salva a media em um arquivo
# temporario, e exibe o log na minha tela.
# Caso contrario desliga o computador pq eu nao to feito fresco
# pra usar uma internet lixo do kct dessa.

echo 'Bla Bla Bla.. Ping SCRIPTER'

function searchPings(){
	# Search Pings of url
	# Enter Url 
	echo 'Enter this URL:'
	touch log.txt
	url=""
	read url
	ping $url -c 4  > log.txt
}
function showLogger(){
	exec 3 < log.txt
	while read arq <&3; do
		echo $arq
	done
}

function getMediaPing(){
	# Get Media of Logger txt
	# Check possible condictions 
	# 1) - if media ping < or == 100
	# 2) if logger is diferent of null;
	# || return 1 if this condictions not satis..
	mec=$(tail -1 log.txt)
	touch aux.txt
	for xd in $mec; do
		conta=$(($conta+1))
		if [ $conta -eq 4 ]; then
			echo $xd > aux.txt
		fi
	done
	meczada=$(cut -c8-9 aux.txt)
	avg=100
	local saida
	if [ $meczada -lt $avg ]; then
		saida=0
		echo $saida
	else
		saida=1
		echo $saida
		return 
	fi
}
searchPings
init=$(getMediaPing)
print='A internet esta do jeito que voce gosta osvaldo'
if [ $init -eq 1 ]; then
	shutdown -h now
else
	echo $print
fi

exit
