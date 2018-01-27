#!/bin/bash

while : ; do
	
	resposta=$( dialog --stdout --title 'Meu menu' --menu 'O que deseja fazer?' 0 0 0  1 'Navegar na internet' 2 'Escrever uma carta' 3 'Jogar paciencia' 4 'Perder tempo' 0 'Sair' )

	#se aperta esc ou cancelar entao sair
	[ $? -ne ] && break

	
	case $resposta in
	
	1) firefox 'http://www.google.com.br' ;;
	2) nano /tmp/carta.txt ;;
	3) /usr/games/solitaire ;;
	4) xsnow ; xeyes ;;
	0) break ;;
	
	esac
done

echo 'vlw!'

