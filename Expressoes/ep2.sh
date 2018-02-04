#!/bin/bash



#grep '[0-9]' /etc/passwd # lista o intervalo de numeros entre 0 e 9 contidos no diretorio

egrep '^.{17,}$' /etc/passwd # lista a linha que contem 17 caracters ou mais independente de quais sejam.

egrep '[0-9]{3,} /etc/passwd | cut -d : -f 1 # lista todos os usuarios com 3 ou mais digitos contidos no intervalo de 0 a 9
