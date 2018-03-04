#!/bin/bash

#######

#How to use: ./generateWordlist.sh > wordlist.txt
#Scripter: lsbloo !
#Adapted for github: linuxchoice.
#


acao=$(dialog --stdout --menu "Generate Wordlist in ShellScript" 8 40 50 generate "GenerateWordlist")
	case $acao in

	generate)
		clear
		( echo 20; sleep 1
  		 echo 40; sleep 1
	 	echo 60; sleep 1
	 	echo 100; sleep 1) |
		dialog --title "Generating.." --gauge "Wait.. Or CTRL+C" 8 40 50
		clear

		string=( {a..z} )
		for x in ${string[@]}; do
		for z in ${string[@]}; do
		for y in ${string[@]}; do
		for w in ${string[@]}; do
		for k in ${string[@]}; do
		echo $x$z$y$w$k
		done done done done done
		;;

	esac	


