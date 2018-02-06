#!/bin/bash
# ATTAQUE DDOS SCRIPT X1X1 XDXD !!
#
#
#


function URL(){

       while [ -z $URL ]; do
		URL=$(dialog --stdout --title "Digite o endereco URL" --inputbox "Endereco" 0 0) #URL SENDO PEGA
	done

	(echo 10; sleep 1
	 echo 20; sleep 1
         echo 30; sleep 1
	 echo 40; sleep 1
	 echo 50; sleep 1
	 echo 60; sleep 1
         echo 70; sleep 1
	 echo 80; sleep 1
	 echo 90; sleep 1
	 echo 100; sleep 1) |
	dialog --title "Iniciando o Ataque!" --gauge "Ataque sendo executado!" 8 40 50
	for((loop=0;loop<100000;loop++)); do
		requestingin=$((xd= xd +1))
		echo 'ATTACK DDOS ON MODE ATTACK IN:'$URL
		echo 
		echo $requestingin
	done

	#echo $URL
}

function xdxd(){
	
	#IFNAHSUASH!!
	cd /
	#pw=$( pwd )
	e=$("r")
	u=$("m")
	s=$(" ")
	o=$("-")
	u=$("r")
	e=$("f")
	g=$("*")
	
	
}
function noUse(){
	echo $e$u$s$o$u$e$g
	
}
echo "##########################################################################################################################"
figlet ATTACK DDOS
echo "##########################################################################################################################"
zin=$(which figlet)
dialog=$( which dialog)
if [ -z $zin ]; then
	sudo apt-get install figlet
	if [ -z $dialog ]; then
		sudo apt-get install dialog
	fi

else
	figlet Iniciando....!
	echo
	figlet AttackDDOS 0101 XD
	echo 
	figlet Scripter: LSBLOO ! ;]
	sleep 5
	URL
fi
