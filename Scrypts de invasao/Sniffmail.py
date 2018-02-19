
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------
#
#     Nome: SniffMail
#
#     Funçao: Web crawler que procura emails pela web, e
#             os armazena em um arquivo de texto.
#
#     Coder: André Ramos
#	
#     Datas- 
#	Versão 1.0: 23/12/2014
#
#-------------------------------------------------------------


import urllib.request
import sys
import os


def obterCodFonte(pgInicial):
    try: 
        pagina = urllib.request.urlopen(pgInicial) #Abrindo a pagina
        texto = pagina.read().decode('latin') #Decodificando pagina 
        return texto
    except:
        return False


def encontrarEmail(texto, provedor):   
    if(texto != False):
        
        while(True):
            emailFim = texto.find(provedor)
            
            if(emailFim > 0):
                emailFim += len(provedor) #Procurando por um email
                emailInicio = emailFim
                
                while(texto[emailInicio] not in ['>', ' ', '"', ';', "'", ':', '/', '\\', '(', ')', '%', '~', '=']): #Procurando inicio do email
                    emailInicio -= 1
                emailInicio += 1

                #Verificando se é um email valido
                if(texto[emailInicio:emailFim] not in emailsEncontrados and texto[emailInicio:emailFim] != ''): #Verificando se é um email valido
                    print('Email Encontrado: ',texto[emailInicio:emailFim])
                    emailsEncontrados.append(texto[emailInicio:emailFim])

                    #Escrevendo email em um arquivo de texto
                    emailsArquivo = open('Emails.txt', 'a')
                    emailsArquivo.write(texto[emailInicio:emailFim]+os.linesep)
                    emailsArquivo.close()
                    
                #Cortando o texto para continuar a busca por emails
                texto = texto[emailFim:len(texto)] 
            else:
                break


def encontrarLinks(texto):
    if(texto != False):

        try:
            from bs4 import BeautifulSoup
        except:
            print(os.linesep+'É necessario instalar a biblioteca BeautifulSoup4 para continuar.'+os.linesep)
            print('Se estiver utilizando Debian/Ubuntu USE: python3 SniffMail.py --install-ubuntu'+os.linesep)
            sys.exit() #Saindo do script
        
        soup = BeautifulSoup(texto)

        links = []

        #Procurando links na pagina
        for link in soup.find_all('a', href=True):
            links.append(link['href'])

        return(links)


if(len(sys.argv) > 1): #Verifica se foi passado algum argumento

    #Opçoes de argumentos
    
        #-h, --help
    if(sys.argv[1] == '--help' or sys.argv[1] == '-h' ):
        print(os.linesep+'Uso: python3 SniffMail.py [LINK].'+os.linesep+'Exemplo: python3 SniffMail.py http://www.google.com.br'+os.linesep+os.linesep)
        print('-h, --help    mostra esta ajuda.'+os.linesep+os.linesep)
        print('-v, --version    informa a versão do script.'+os.linesep+os.linesep)
        print('--install-ubuntu   Instala a biblioteca Beautiful Soup no Debian/Ubuntu.'+os.linesep+os.linesep)
        print('Função: Este script tem a funçao de varrer a internet em busca de emails, e os salvar em um arquivo texto.')
        print('Este arquivo, será salvo no mesmo diretório que se localiza este script, em: '+ os.getcwd()+os.linesep+os.linesep)
    else:
        
        #-v, --version
        if(sys.argv[1] == '-v' or sys.argv[1] == '--version'):
              print(os.linesep+'SniffMail 1.0'+os.linesep)   
        else:

            #--instal-ubuntu
            if(sys.argv[1] == '--install-ubuntu'):
                os.system('sudo sudo apt-get install python3-bs4')
            else:
                    
                #Execuçao do script
                linksEncontrados = [sys.argv[1]]
                global emailsEncontrados
                emailsEncontrados = []

                print(os.linesep)
        
                for linkAtual in linksEncontrados:
    
                    try:
                        texto = obterCodFonte(linkAtual)
    
                        #Capturando links
                        for link in encontrarLinks(texto):
                            if link not in linksEncontrados:
                                linksEncontrados.append(link)

                        #Capturando emails
                        for provedor in ['@gmail.com', '@hotmail.com', '@outlook.com', '@live.com', '@yahoo.com.br', '@yahoo.com', '@bol.com.br', '@uol.com.br', '@msn.com', '@ig.com.br', '@globomail.com', '@oi.com.br', '@pop.com.br', '@inteligweb.com.br', '@r7.com', '@folha.com.br', '@zipmail.com.br']:
                            encontrarEmail(texto, provedor)

                    except:
                        linksEncontrados.remove(linkAtual) #Removendo da lista link invalido
                        continue
else:
    print(os.linesep+'Falta argumentos. Use o comando: python3 SniffMail.py --help'+os.linesep+os.linesep+'Digite --help para mais detalhes de sintaxe'+os.linesep)
    
    

    #Status API Training Shop Blog About 

    #© 2015 GitHub, Inc. Terms Privacy Security Contact 

