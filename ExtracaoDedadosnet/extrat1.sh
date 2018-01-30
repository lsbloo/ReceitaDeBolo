#!/bin/bash
#
#

URL="https://pt.wikipedia.org/wiki/Tibia#O_crescimento_do_jogo"
#Padrao linhas que inicicam com maiusculas
#echo $URL
lynx -dump -nolist $URL |grep '[a-z]' > dad.txt


