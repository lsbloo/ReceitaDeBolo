#!/bin/bash
#Filtrando dados do /etc/passwd

# metacaracter ^ = filtra  pela palavra no inicio da linha exemplo ^root
# \\ $ = representa o fim de uma linha exemplo bash$
		# obs: usar a expressao '^$' representa encontrar uma linha vazia pq estamos procurando o comeco e o fim da linha ao mesmo tempo.
# \\ [] = listas usado quando se quer procurar uma quantidade de variacoes na string exemplo '[Oo]svaldo'
touch palavras.txt

grep '^[aeiou]' /etc/passwd > palavras.txt # indica que vamos pesquisar por palavras que tenham vogais no comeco da linha..

cat palavras.txt
