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
	comB="commitBranch"
	#verificar o diretorio do repositorio, da o git status pra exibir arquivos , pedi o nome do branch
	# da o commit 
	# usar o git config caso ele nao tenha configurado a maquina
	# da o push
	if [ $chose == $comB ]; then
		diretorioAtual=$(pwd)
		dialog --title "Seu diretorio Atual" --msgbox $diretorioAtual 10 100
		dialog --stdout --title "Continuar no Diretorio?" --yesno '\n Você deseja continuar no diretorio Atual?' 10 50
		if [ $? -eq 0 ]; then
			echo 'Status Atual do seu REPOSITORIO'
			echo '----------------------------------------------------------------------'
			echo 
			echo
			git status
			sleep 5
			echo ''
			nomeBranch=$(dialog --stdout --title "Nome Branch" --inputbox 'Digite o nome da branch' 10 50)
			nomeCommit=$(dialog --stdout --title "Nome Commit" --inputbox 'Digite o nome do seu commit' 10 50)
			while [ -z $nomeBranch -a -z $nomeCommit ]; do
				dialog --title "Preencha os campos corretamente" --msgbox "Preencha os campos corretamente" 10 100
				nomeBranch=$(dialog --stdout --title "Nome Branch" --inputbox 'Digite o nome da branch' 10 50)
                        	nomeCommit=$(dialog --stdout --title "Nome Commit" --inputbox 'Digite o nome do seu commit' 10 50)
			done
			email=$(dialog --stdout --title "Email User" --inputbox 'Digite o seu email:' 10 50)
			while [ -z $email ]; do
				email=$(dialog --stdout --title "Email User" --inputbox 'Digite o seu email:' 10 50)
			done
			git --config user.email $email
			git add *
			git checkout -b $nomeBranch
			git commit -m $nomeCommit
			sleep 2
			clear
			git push --set-upstream origin $nomeBranch
			sleep 1
			exit 0
		else
			novoDiretorio=$(dialog --stdout --title "Entra no Diretorio" --inputbox 'Digite o caminho do diretorio' 10 50)
			while [ -z $novoDiretorio ]; do
				novoDiretorio=$(dialog --stdout --title "Entra no Diretorio GITHUB" --inputbox 'Digite o caminho do diretorio GITHUB' 10 50)
			done
			cd $novoDiretorio
			echo 'Status Atual do seu REPOSITORIO'
			echo '----------------------------------------------------------------------'
			echo 
			echo
			git status
			sleep 5
			echo ''
			nomeBranch=$(dialog --stdout --title "Nome Branch" --inputbox 'Digite o nome da branch' 10 50)
			nomeCommit=$(dialog --stdout --title "Nome Commit" --inputbox 'Digite o nome do seu commit' 10 50)
			while [ -z $nomeBranch -a -z $nomeCommit ]; do
				dialog --title "Preencha os campos corretamente" --msgbox "Preencha os campos corretamente" 10 100
				nomeBranch=$(dialog --stdout --title "Nome Branch" --inputbox 'Digite o nome da branch' 10 50)
                        	nomeCommit=$(dialog --stdout --title "Nome Commit" --inputbox 'Digite o nome do seu commit' 10 50)
			done
			email=$(dialog --stdout --title "Email User" --inputbox 'Digite o seu email:' 10 50)
			while [ -z $email ]; do
				email=$(dialog --stdout --title "Email User" --inputbox 'Digite o seu email:' 10 50)
			done
			git --config user.email $email
			git add *
			git checkout -b $nomeBranch
			git commit -m $nomeCommit
			sleep 2
			clear
			git push --set-upstream origin $nomeBranch
			sleep 1
			exit 0	
		fi

	fi

}
function clone(){
 	cloneRep="cloneRepo"
	if [ $chose == $cloneRep ]; then
		diretorio=$(dialog --stdout --title "Escolha o diretorio destino do clone" --inputbox 'Diretorio' 10 50)
		if [ -z $diretorio ]; then
			dialog --title "Error" --msgbox 'Preencha o campo corretamente' 10 50
			while [ -z $diretorio ]; do
				diretorio=$(dialog --stdout --title "Escolha o diretorio destino do clone" --inputbox 'Diretorio' 10 50)
			done
			if [ -n $diretorio ]; then
				#link=$(dialog --stdout --title "Link GITHUB" --inputbox 'Link aqui \/' 10 30)
				clear
				echo '-----------------------------------------------------------------------'
				echo 
				echo 'PREENCHA O LINK DO GITHUB AQUI NO TERMINAL'
				echo '-----------------------------------------------------------------------'
				echo
				echo 'Copie o link aqui embaixo'
				read link
			fi
		else
			#link=$(dialog --stdout --title "Link GITHUB" --inputbox 'Link aqui \/' 10 30)
			clear
		       echo '-----------------------------------------------------------------------'
                       echo 
                       echo 'PREENCHA O LINK DO GITHUB AQUI NO TERMINAL'
                       echo '-----------------------------------------------------------------------'
                       echo
                       echo 'Copie o link aqui embaixo'

		
			read link
			if [ -z $link ]; then
				dialog --title "Error" --msgbox 'Preencha o campo corretamente' 10 50
				while [ -z $link ]; do
					#link=$(dialog --stdout --title "Link GITHUB" --inputbox 'Link aqui \/' 10 30)
					 clear
        		               echo '-----------------------------------------------------------------------'
		                       echo 
                      			 echo 'PREENCHA O LINK DO GITHUB AQUI NO TERMINAL'
                       			echo '-----------------------------------------------------------------------'
                       			echo

					read link
				done
				if [ -n $link ]; then
					#link=$(dialog --stdout --title "Link GITHUB" --inputbox 'Link aqui \/' 10 30)
					 clear
		                         echo '-----------------------------------------------------------------------'
                		         echo 
                       			 echo 'PREENCHA O LINK DO GITHUB AQUI NO TERMINAL'
                       			 echo '-----------------------------------------------------------------------'
                      			 echo

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
				exit 0
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
clone
commitB
