#!/bin/bash

dialog --yesno 'sim ou nao?' 0 0 ; echo Retorno: $?

dialog --yesno 'Quer ver as horas?' 0 0 

if [ $? -eq 0 ]; then
	data=$(date)
	echo 'Agora sao': $data

else
	echo ' ok'

fi

