
#!/bin/bash
acao=$( dialog --stdout --menu "Gerenciador de usuarios" 0 0 0 adicionar "Adicionar usuarios" lista "Lista usuarios" remove "Remove usuarios" )


case "$acao" in #aguarda a opcao listar ou remover

adicionar)
	#echo 'ok'
	login=$( dialog --stdout --inputbox "Digite o login: " 0 0 ) #Entrada de texto que armazena o login do usuario na variavel login
#	echo $login	
	verificalogs=$( cat logs.txt ) # armazena na variavel todos os logins salvo no txt
	if [ -z $verificalogs ]; then # verifica se esta vazio a variavel
		#echo 'Arquivo vazio!'
		#echo 'Antes de Adicionar -Favor carregar arquivo logs.txt na opcao Listar'
		dialog --title "Usuario" --msgbox "Favor carregar logs.txt na opcao Listar" 20 30
	else
		if [ -z $login ]; then #caso contrario , verifica se o login é vazio..
			echo 'sem usuario'
		else
			verificausuario=$( grep -i $login logs.txt ) #caso contrario , verifica se o login do usuario ja existe no arquivo logs com o comando grep
			#echo $verificausuario
			if [ -z $verificausuario ]; then # caso seja nula entao ele cria um novo usuario
				echo 'Aguarde..'
				sudo adduser $login
				
				dialog --title "Usuario" --msgbox "Concluido" 0 0 

			else
				dialog --title "Usuario" --msgbox "Usuario ja existe" 0 0
				#echo 'usuario ja existe' #senao o usuarioja existe
			fi

		fi


	fi


	;; #similar ao break; do case convencional das linguagens de programacao Java,C


lista)
	#lista todos os campos de login
	#temp=$( dialog --textbox /etc/passwd 0 0 )
	#criei um arquivo para salvar os logs do arq /etc/passwd
	touch logs.txt
	#usei o cut  cortando o ponto e pegando a primeira coluna no caso o nome da pessoa e enviei com o sed para o arquivo de logs.txt
	cut -d':' -f1 /etc/passwd | sed 1d > logs.txt
	# aqui criei um tittle dos usuarios com uma caixa de texto com os dados contidos no arquivo logs.txt com dimensao de 20x30
	dialog --title "Usuarios" --textbox logs.txt 20 30 
	
	#rm -rf $temp
	;;

remove)
	echo 'A implementar!'
		
    	;;
esac
