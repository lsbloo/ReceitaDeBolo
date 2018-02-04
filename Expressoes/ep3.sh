#!/bin/bash

#liste todos os UID do arquivo /etc/passwd
	#egrep '[0-9]{3}' /etc/passwd | cut -d : -f 3

#liste todos os Usuarios do arquivo /etc/passwd

#	egrep '^[a-z]' /etc/passwd | cut -d : -f 1
# Faça uma expressao para deletar n quantidades.txt de um diretorio , crie o diretorio e coloque os txt dentro dele
	
	#mkdir meusTxt
	dir="meusTxt"
	cd $dir
	for((loop=0;loop<5;loop++)); do
		echo 'Digite o nome do txt'
		read nome
		touch $nome".txt"
	done
	rm -i *.txt



