#init
from prof import *


#Regras
    # se a entrada do usuario em empreendedor exemplo for 2 e a da vocaçao dele for 2 tambem , entao e considerado "bom"
    # se a entrada do usuario em empreendedor exemplo for 1 e a da vocacao dele for 3 , entao e considerado Tem , mas nao e bom
    # se a entrada do usuario em empreendedor exemplo for 0 e a da vocacao dele for 3 , entao nao tem .
def tabela_prof():
    print()
    print()
    print("WebMaster")                 
    print("Empreendedor")
    print("GerenteProjetos")
    print("AdministradorSeguranca")                   ,
    print("CientistaDados")                 
    print("WebDesigner")
    print("ArquitetoSoftware")
    print('AnalistaBi')
    print("GerenteRedes")                      ,
    print("EngenheiroSoftware")                   
    print("AnalistaTestes")                 
    print("AnalistaNegocios")                      ,
    print("FrontEndDEV")
    print("Professor")
    print("DevConteudoEducacional")
    print("Programador")
    print("AnalistaSistema")
    print("EngenheiroSoftware")
    print()
    print()
                       

    

          
def show_menu():
        print("-------------------------------------------------")
        print("com base na teorioa de Holland,procure suas profissao")
        print()
        print("-----------------------------------------------------")
        print("Exemplo entrada: Profissao: Programador Empreendedor:1 , Social: 3 , Convencional: 1, Realista: 0, Artistica: 0, Investigativa: 2")
        print("Exemplo2 entrada: programador 1 3 1 0 0 2 ")
        print()
        print("OBS: os dados de entrada nao podem totalizar numeros maiores que 10")
        print()

def input_user():
    global lista_entradas
    lista_entradas=[]
    
    profissao,empreendedor,social,convencional,realista,artistica,investigativa = input().split(" ")

    lista_entradas.append([profissao,empreendedor,social,convencional,realista,artistica,investigativa])
    #lista_entradas = input.split(" ")

    return lista_entradas

def search_your_voc():
    global save
    global dados
    global numeros_save
    dados =''
    numeros_padrao=["0","1","2","3","4","5","6","7","8","9"]
    vocacao_pes=''
    numeros_save=[]
    cont=0
    string=''
    for profissoes in range(len(list_profissoes)):
        #print(list_profissoes[profissoes].get(lista_entradas[0][0]))
        saida_prof = list_profissoes[profissoes].get(lista_entradas[0][0])
        if saida_prof == lista_entradas[0][0]:
            #print(list_profissoes[profissoes].items())
            save = list_profissoes[profissoes].items()
            for k in lista_entradas:
                for z in k:
                    dados+=z
                    #print(z, end=" ")

    for k in save:
        for xd in k:
            cont +=1
            if cont == 2:
                string+=str(xd)
                cont = 0
    for xd in string:
        if xd.isdigit():
            numeros_save.append(xd)

    return save,dados,numeros_save


def compare_tab_input(save,dados,numeros_save,list_profissoes):
    dados_num=[]
    diferenca_empreendedor=0
    diferenca_social=0
    diferenca_convencional=0
    diferenca_realista=0
    diferenca_artistica=0
    diferenca_investigativa=0

    """
    Entrada usuario : empreendedor indice 0 , social 1, convencional 2, realista 3, artistica 4, investigativa 5
     """
    #print("numerosSave:",numeros_save)
    #print("Dados do Programa: ",dados)
    #print()
    for xd in dados:
        if xd.isdigit():
            dados_num.append(xd)



    print()
    print("Dados salvos Sobre: ",lista_entradas[0][0])
    for x in save:
        print(x)


    print()
    print()

    print("Resultado -------------------------------------------------------- ")


    for profissoes in range(len(list_profissoes)):
        #print(list_profissoes[profissoes].get(lista_entradas[0][0]))
        saida_prof = list_profissoes[profissoes].get(lista_entradas[0][0])
        if saida_prof == lista_entradas[0][0]:
            empreendedor = list_profissoes[profissoes].get("Empreendedor")
            social = list_profissoes[profissoes].get("Social")
            convencional = list_profissoes[profissoes].get("Convencional")
            realista = list_profissoes[profissoes].get("Realista")
            artistica = list_profissoes[profissoes].get("Artistica")
            investigativa = list_profissoes[profissoes].get("Investigativa")
            
            """
            print(empreendedor)
            print(social)
            print(convencional)
            print(realista)
            print(artistica)
            print(investigativa)
            """

    if int(dados_num[0]) != int(empreendedor):
        diferenca_empreendedor = int(dados_num[0]) - int(empreendedor)
    

    if int(dados_num[1]) != int(social):
        diferenca_social = int(dados_num[1]) - int(social)
  

    if int(dados_num[2]) != int(convencional):
        diferenca_convencional = int(dados_num[2]) - int(convencional)
   
         
    if int(dados_num[3]) != int(realista):
        diferenca_realista = int(dados_num[3]) - int(realista)
   

    if int(dados_num[4]) != int(artistica):
        diferenca_artistica = int(dados_num[4]) - int(artistica)
    

    if int(dados_num[5]) != int(investigativa):
        diferenca_investigativa = int(dados_num[5]) - int(investigativa)
    


    #print(diferenca_empreendedor)
    #print(diferenca_social)
    #print(diferenca_convencional)
    #print(diferenca_realista)
    #print(diferenca_artistica)
    #print(diferenca_investigativa)

    

    print()
    print("Empreendedor:")
    
    if diferenca_empreendedor == -2:
        print("Empreendedor -Pode ser!")
    elif diferenca_empreendedor == -1:
        print("Empreendedor , correto!")
    elif diferenca_empreendedor == -3:
        print("Empreendedor , existe uma possibilidade!")
    elif diferenca_empreendedor == -4:
        print("Nao e sua profissao!")
    elif diferenca_empreendedor == 0:
        print("bom!")
    elif diferenca_empreendedor >= 1:
        print("Competencia Adicional!")
    else:
        print("error!")


    print()
    print("Social")
    
    if diferenca_social == -2:
        print("Social  -Pode ser!")
    elif diferenca_social == -1:
        print("Social , correto!")
    elif diferenca_social == -3:
        print("Social , existe uma possibilidade!")
    elif diferenca_social == -4:
        print("Nao e sua profissao!")

    elif diferenca_social == 0:
        print("bom!")
    elif diferenca_social >= 1:
        print("Competencia Adicional!")
        
    else:
        print("error!")

    print()    
    print("Convencional!")
    
    if diferenca_convencional == -2:
        print("Convencional  -Pode ser!")
    elif diferenca_convencional == -1:
        print("Convencional , correto!")
    elif diferenca_social == -3:
        print("Convencional , existe uma possibilidade!")
    elif diferenca_convencional == -4:
        print("Nao e sua profissao!")
    elif diferenca_convencional == 0:
        print("bom!")
    elif diferenca_convencional >= 1:
        print("Competencia Adicional!")
    else:
        print("error!")

    print()
    print("Realista")
   
    if diferenca_realista == -2:
        print("Realista  -Pode ser!")
    elif diferenca_realista ==-1:
        print("Realista , correto!")
    elif diferenca_realista ==-3:
        print("Realista , existe uma possibilidade!")
    elif diferenca_realista == -4:
        print("Nao e sua profissao!")
    elif diferenca_realista == 0:
        print("bom!")
    elif diferenca_realista >= 1:
        print("Competencia Adicional!")
    else:
        print("error!")

    print()
    print("Artistica")
    
    if diferenca_artistica == -2:
        print("Artistica  -Pode ser!")
    elif diferenca_artistica == -1:
        print("Artistica , correto!")
    elif diferenca_artistica == -3:
        print("Artistica , existe uma possibilidade!")
    elif diferenca_artistica == -4:
        print("Nao e sua profissao!")
    elif diferenca_artistica == 0:
        print("bom!")

    elif diferenca_artistica >= 1:
        print("Competencia Adicional!")
    else:
        print("error!")

    print()
    print("Investigativa")
    
    if diferenca_investigativa == -2:
        print("Investigativa  -Pode ser!")
    elif diferenca_investigativa == -1:
        print("Investigativa , correto!")
    elif diferenca_investigativa == -3:
        print("Investigativa , existe uma possibilidade!")
    elif diferenca_investigativa == -4:
        print("Nao e sua profissao!")
    elif diferenca_investigativa == 0:
        print("bom!")
    elif diferenca_investigativa >= 1:
        print("Competencia Adicional!")
    else:
        print("error!")
    
    
    


tabela_prof()
show_menu()
input_user()
search_your_voc()
compare_tab_input(save,dados,numeros_save,list_profissoes)
