#!/bin/bash
#Script que fornece uma interface Grafica para commits no gitHUB;
#Automatizar upload de dados no github sem a necessidade de comandos GIT;

function exeDependences(){
	dialog=$(which dialog)
	ver="/usr/bin/dialog"
	if [ $ver == $dialog ]; then
		echo 'dialoginstalado'
	else
	 	echo $ver
		echo $dialog
		dialog --title "Instalando dependencia!" --msgbox 'Instalando a interface Dialog' 5 30
	fi
	return 1
}
function user_ch(){
	if [ -z $verifica ]; then
		echo 'error dialog'
	else
		#echo 'usuario escolhe opcao'
		#usuario escolhe opcao!
		opcao=$(dialog --stdout --title "Escolha sua opção!" --menu 'Escolha o que deseja fazer' 10 50 50 commitBranch 'Commit criando sua Branch?' commitMaster 'Commit criando sua Master?' cloneRepo    'Clonar um Repositorio?')
		echo $opcao		
	fi
	return 2;
}
function commitB(){
 	branch="commitBranch"
	if [ $chose == $branch ]; then
		diretorio=$(dialog --stdout --title "Escolha o diretorio destino do clone" --inputbox 'Diretorio' 10 50)
		if [ -z $diretorio ]; then
			dialog --title "Error" --msgbox 'Preencha o campo corretamente' 10 50
			while [ -z $diretorio ]; do
				diretorio=$(dialog --stdout --title "Escolha o diretorio destino do clone" --inputbox 'Diretorio' 10 50)
			done
			if [ -n $diretorio ]; then
				#link=$(dialog --stdout --title "Link GITHUB" --inputbox 'Link aqui \/' 10 30)
				echo 'Copie o link aqui embaixo'
				read link
			fi
		else
			#link=$(dialog --stdout --title "Link GITHUB" --inputbox 'Link aqui \/' 10 30)
			echo 'Copie o link aqui embaixo'
			read link
			if [ -z $link ]; then
				dialog --title "Error" --msgbox 'Preencha o campo corretamente' 10 50
				while [ -z $link ]; do
					#link=$(dialog --stdout --title "Link GITHUB" --inputbox 'Link aqui \/' 10 30)
					echo 'Copie o link aqui embaixo'
					read link
				done
				if [ -n $link ]; then
					#link=$(dialog --stdout --title "Link GITHUB" --inputbox 'Link aqui \/' 10 30)
					echo 'Copie o link aqui embaixo'
					read link
				fi
			else
				dialog --title 'Clonando Repositorio' --gauge 'Clonando Repositorio...' 8 40 60 100
				sleep 1
				clear
				cd $diretorio
				git clone $link
				#sleep 2
				dialog --title 'Clonado' --msgbox 'Operação finalizada' 10 50
			fi

		fi

	else
		echo 'error Branch'
	fi
}
verifica=$(exeDependences)
#echo 'valor' $verifica
chose=$(user_ch)
echo $chose
commitB
