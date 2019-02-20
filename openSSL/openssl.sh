#!/bin/bash
# openssl scripter;

function generatessl_key(){
	arq_par_key = ""
	bits_key_par=""
	echo "Digite o nome do arquivo par de chaves extensao .key"
	read arq_par_key
	echo "Digite o tamanho bits da chave "
	read bits_key_par
	if [ -z $arq_par_key || -z $bits_key_par ]; then
		echo "Digite corretamente."
	else
		openssl genrsa -out $arq_par_key $bits_key_par
		
	fi

}
function viewssl_key() {
	arq_par_key=""
	echo "Digite o nome do arquivo com extensao .key"
	read arq_par_key
	if [ -z $arq_par_key]; then
		echo "Digite corretamente."
	else
		openssl rsa -in $arq_par_key
	fi
}
function export_key_public() {
	arq_par_key=""
	arq_par_key_pub=""
	echo "Digite o nome do arquivo par de chaves" 
	read arq_par_key
	echo "Digite o nome do arquivo a ser criado com a chave publica"
	read arq_par_key_pub
	if [ -z $arq_par_key || -z $arq_par_key_pub ]; then
		echo "Digite corretamente!"
	else
		openssl rsa -in $arq_par_key -pubout -out $arq_par_key_pub
	fi

}
function criph_message(){
	arq_par_key=""
	arq_criph_message=""
	key_public_send=""
	echo "Digite o nome do arquivo a ser cifrado"
	read arq_par_key
	echo "Digite o nome do arquivo cifrado"
	read arq_criph_message
	echo "Digite a chave publica do destinatario"
	read key_public_send
	if [ -z $arq_par_key || -z $arq_criph_message || -z $key_public_send ]; then
		echo "Digite corretamente!"
	else
		openssl rsautl -in $arq_par_key -out $arq_criph_message -inkey $key_public_send -pubin -encrypt
	fi


}
function decriph_message(){
	arq_par_key=""
        arq_criph_message=""
        key_private_your=""
	echo "Digite o nome do arquivo cifrado!"
	read arq_par_key
	echo "Digite o nome do arquivo gerado decifrado"
	read arq_criph_message
	echo "Digite a sua chave privada"
	read key_private_your
	if [ -z $arq_par_key || -z $arq_criph_message || -z $key_private_your ]; then 
		echo "Digite corretamente!"
	else
		openssl rsautl -in $arq_par_key -out $arq_criph_message -inkey $key_private_your -decrypt
	fi
}
function generate_ass(){
	arq_ass=""
	arq_save_ass=""
	arq_private_key=""
	echo "Digite o nome do arquivo a ser assinado"
	read arq_ass
	echo "Digite o nome do arquivo que armazenara a assinatura"
	read arq_save_ass
	echo "Digite o nome do arquivo que contem a chave privada"
	read arq_private_key
	if [ -z $arq_ass || -z $arq_save_ass || -z $arq_private_key ]; then
		echo "Digite corretamente!"
	else
		openssl rsautl -sing -in $arq_ass -out $arq_save_ass -inkey $arq_private_key -pkcs
	fi	
}
function check_ass(){
	arq_save_ass=""
	arq_public=""
	arq_recovery=""
	echo "Digite o nome do arquivo contendo a assinatura"
	read arq_save_ass
	echo "DIgite o nome do arquivo contendo a chave publica"
	read arq_pubic
	echo "Digite o nome do arquivo a ser recuperado pela assinatura!"
	read arq_recovery
	if [ -z $arq_save_ass || -z $arq_public || -z $arq_recovery ]; then
		echo "Digite corretmente!"
	else
		openssl rsautl -verify -in $arq_save_ass -inkey $arq_public -pubin -pkcs -out $arq_recovery
	fi
}


echo "Digite [1] - gerar ssl key , [2]- visualizar ssl key , [3] - exportar a chave public , [4] -criptografar messagem , [5] - decript messagem "
echo "[6] - gerar assinatura , [7] - checar assinatura"
read opcao
if [ $opcao -eq 1 ]; then
	generatessl_key
elif [ $opcao -eq 2 ]; then
	viewssl_key
elif [ $opcao -eq 3 ]; then
	export_key_public
elif [ $opcao -eq 4 ]; then
	criph_message
elif [ $opcao -eq 5 ]; then
	decriph_message
elif [ $opcao -eq 6 ]; then
	generate_ass
elif [ $opcao -eq 7 ]; then
	check_ass
else
	echo "FODA-SE!"

fi

