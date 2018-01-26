 #!/bin/bash
#-------------------------------------------------
#	Scripter: lsbloo
#------------------------------------------------

killProcess(){
	top
	echo 'Digite o Pid do processo'
	read pid
	while [ -z $pid ]; do
		echo 'Digite o id corretamente'
		read pid

	done
	kill -9 $pid
	echo 'Processo encerrado'

}

vmStart(){
	sudo apt-get install vmstat
	vmstat
}
dioStart(){
	sudo apt-get install dstat
	dstat -cm
}
echo 'Bem vindo'
echo 'Selecione a opcao'
echo 'Matar processo PID [1] ,  informacoes sobre processos [2] , [3] monitoramento de perfomace'
read opcao

if [ $opcao -eq 1 ]; then
	killProcess
elif [ $opcao -eq 2 ]; then
	vmStart

elif [ $opcao -eq 3 ]; then
	dioStart

else
	echo 'Fim'
fi


