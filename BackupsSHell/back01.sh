#!/bin/bash
	#Script de backUPsimples !:|
#!!


dialog=$(which dialog )
verifica="/usr/bin/dialog"
MYDIR=$( pwd )
#echo $dialog
#echo $verifica
#echo $MYDIR

if [ $dialog==$verifica ]; then
	echo 'ok'
else
	dialog --msgbox "Dialog nao encontrado em" 10 40
        sudo apt-get install dialog
fi

function menu_main(){
	inf_eq=0
	while [ $inf_eq -eq 0 ]; do
				menu_pegaAcao=$( dialog --stdout --menu "BackupsDir" 10 50 60 realizarBackup "Realizar Backup" removerArq "Remover aquivo especificado")
				if [ -z menu_pegaAcao ]; then
						echo '0'
				else
					inf_eq=1
				fi

	done
}
menu_main
function removerArqxDir(){
		acao=$( dialog --stdout --title 'Remover' --radiolist 'Diretorio ou arquivo?' 20 20 20 diretorio 'Diretorio' off  arquivo 'Arquivo' off )
		
		case $acao in
		
		diretorio)
			nome_diretorio=$( dialog  --stdout --inputbox "Digite o nome do diretorio" 10 10 )
			if [ -z $nome_diretorio ]; then
				echo 'y'
			else
				rmdir $MYDIR"/"$nome_diretorio
                                dialog --msgbox "Concluido!" 30 30
			fi

			;;
		arquivo)
			nome_arquivo=$( dialog --stdout --inputbox "Digite o nome do arquivo!" 10 10)
			if [ -z $nome_arquivo ]; then
				echo 'z'
			else
				rm $MYDIR"/"$nomearquivo
                                dialog --msgbox "Concluiido!" 30 30

			fi

		esac		

}
function realizarBack(){
		DIRETORIO_ORIGEM=$( dialog --stdout --inputbox "Digite o caminho diretorio origem" 10 10 )
		NOMEARQUIVO=$( dialog --stdout --inputbox "Digite o nome do arquivo BAckup .Tar" 10 10 )
		DIRETORIO_DESTINO=$( dialog --stdout --inputbox "Digite o caminho diretorio destino" 10 10)

		if [ -z DIRETORIO_ORIGEM || -z DIRETORIO_DESTINO || -z NOMEARQUIVO ]; then
				dialog --msgbox "Error preencha os campos corretamente" 30 30
		else
			sleep 2
			( echo 40 ; sleep 2
			  echo 70 ; sleep 1
			  echo 100 ; sleep 1 ) | dialog --title "Em Andamento..." --gauge "Backup..." 8 40 60
			tar -cvf ${NOMEARQUIVO} ${DIRETORIO_ORIGEM}
			gzip  $NOMEARQUIVO
			new_name=$NOMEARQUIVO".gz"
			mv $MYDIR"/"$new_name $DIRETORIO_DESTINO
			dialog --msgbox "Concluido!" 30 30
			
		fi

}
case $menu_pegaAcao in

realizarBackup)
		realizarBack
		;;

removerArq)
		removerArqxDir
		;;
esac



