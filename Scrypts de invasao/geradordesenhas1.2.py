import random
def Gerador_numero_frente(qnt,nome_wordlist,num_digitos):
    """
    Funcao que Gera senhas aleatorias com ordem ("numeros"+strings)
    
    """
    inf=0
    helpi = 0
    cont_iguais = 0
    cont_diferentes = 0
    global nome_digitado
    senha_gerada = open(nome_wordlist,"w")
    for i in range(qnt):
        aux = random.choice(alfabeto)
        aux1= random.choice(alfabeto)
        aux2 = random.choice(alfabeto)
        aux3= random.choice(alfabeto)
        aux4= random.choice(alfabeto)
        j = random.choice(numbers)
        n = random.choice(numbers)
        f = random.choice(numbers)
        z = random.choice(numbers)
        w = random.choice(numbers)
        x = random.choice(numbers)
        temp = j+n+f+z+w+x+aux+aux1+aux2+aux3+aux4
        if len(temp) <= len(num_digitos):
            inf +=1
        else:
            temp = temp[1:10]
            nome_digitado+=temp
            aux_temp = nome_digitado
            aux_nome = aux_temp
            if aux_nome != nome_digitado:
                cont_iguais += 1
            else:
                cont_diferentes +=1
            print(nome_digitado,file=senha_gerada)
            file=senha_gerada
            nome_digitado = ''
    
    print("Senhas iguais >",cont_iguais)
    print("Senhas diferentes >",cont_diferentes)
    senha_gerada.close()
def text_frente(qnt,nome_wordlist,qnt_dig):
    
    """
    Funcao que Gera senhas aleatorias com ordem (strings+"numeros")
    """
    inf=0
    helpi = 0
    cont_iguais = 0
    cont_diferentes = 0
    global nome_digitado
    senha_gerada = open(nome_wordlist,"w")
    
    for i in range(qnt):
        aux = random.choice(alfabeto)
        aux1= random.choice(alfabeto)
        aux2 = random.choice(alfabeto)
        aux3= random.choice(alfabeto)
        aux4= random.choice(alfabeto)
        j = random.choice(numbers)
        n = random.choice(numbers)
        f = random.choice(numbers)
        z = random.choice(numbers)
        w = random.choice(numbers)
        x = random.choice(numbers)
        temp = aux+aux1+aux2+aux3+aux4+j+n+f+z+w+x
        if len(temp) <= len(num_digitos):
            inf +=1
        else:
            temp = temp[1:10]
            nome_digitado+=temp
            aux_temp = nome_digitado
            aux_nome = aux_temp
            if aux_nome != nome_digitado:
                cont_iguais += 1
            else:
                cont_diferentes +=1
            print(nome_digitado,file=senha_gerada)
            file=senha_gerada
            nome_digitado = ''
    
    print("Senhas iguais >",cont_iguais)
    print("Senhas diferentes >",cont_diferentes)
    senha_gerada.close()
def text_frente_cruzado(qnt,nome_wordlist,qnt_dig):
    
    """
    Funcao que Gera senhas aleatorias com ordem (strings+"numeros")
    Exemplo: 1t3k5v;
    """
    inf=0
    helpi = 0
    cont_iguais = 0
    cont_diferentes = 0
    global nome_digitado
    senha_gerada = open(nome_wordlist,"w")
    
    for i in range(qnt):
        aux = random.choice(alfabeto)
        aux1= random.choice(alfabeto)
        aux2 = random.choice(alfabeto)
        aux3= random.choice(alfabeto)
        aux4= random.choice(alfabeto)
        j = random.choice(numbers)
        n = random.choice(numbers)
        f = random.choice(numbers)
        z = random.choice(numbers)
        w = random.choice(numbers)
        x = random.choice(numbers)
        temp = w+aux+j+aux2+n+aux4+z+w+x
        if len(temp) <= len(num_digitos):
            inf +=1
        else:
            temp = temp[1:10]
            nome_digitado+=temp
            aux_temp = nome_digitado
            aux_nome = aux_temp
            if aux_nome != nome_digitado:
                cont_iguais += 1
            else:
                cont_diferentes +=1
            print(nome_digitado,file=senha_gerada)
            file=senha_gerada
            nome_digitado = ''
    
    print("Senhas iguais >",cont_iguais)
    print("Senhas diferentes >",cont_diferentes)
    senha_gerada.close()
def Nome_mais_num(nome_dig,qnt,nome_wordlist):
    """
    Funcao que Gera Strings Aleatorias a partir do nome dado
    Salva em um arquivo na pasta local do programa
    parametro nome e quantidade de iteracoes !
    """
    global nome_digitado
    senha_gerada = open(nome_wordlist,"w")
    
    for i in range(qnt):
        j = random.choice(numbers)
        n = random.choice(numbers)
        f = random.choice(numbers)
        z = random.choice(numbers)
        temp = j+n+f+z
        nome_digitado+=nome_dig+temp
        print(nome_digitado,file=senha_gerada)
        file = senha_gerada
        nome_digitado = ''

    
    senha_gerada.close()
def Num_mais_nome(nome_dig,qnt,nome_wordlist):
    global nome_digitado
    senha_gerada = open(nome_wordlist,"w")
    
    for i in range(qnt):
        j = random.choice(numbers)
        n = random.choice(numbers)
        f = random.choice(numbers)
        z = random.choice(numbers)
        temp = j+n+f+z
        nome_digitado+=temp+nome_dig
        print(nome_digitado,file=senha_gerada)
        file = senha_gerada
        nome_digitado = ''

    
    senha_gerada.close()
    
def new_WordList(test,opcao):
    if opcao == "1":
        test = str(input("Criar outra WordList: > [S/N]: ")).upper()
        sair = True
        while(sair):
            if test == "S" or test == "sim":
                nome_wordlist = str(input("Nome da wordlist com extensao .txt !>  "))
                qnt = int(input("Tamanho da wordlist! > "))
                Gerador_numero_frente(qnt,nome_wordlist,num_digitado)
                sair = str(input("Sair [s]: ")).upper()
                if sair == "S":
                    print("Fim Sciprit [+] ")
                    break
            else:
                print("Fim Script [+] ")
                break
    elif opcao == "2":
        test = str(input("Criar outra WordList: > [S/N]: ")).upper()
        sair = True
        while(sair):
            if test == "S" or test == "sim":
                nome_wordlist = str(input("Nome da wordlist com extensao .txt !>  "))
                qnt = int(input("Tamanho da wordlist! > "))
                text_frente(qnt,nome_wordlist,qnt_dig)
                sair = str(input("Sair [s]: ")).upper()
                if sair == "S":
                    print("Fim Sciprit [+] ")
                    break
            else:
                print("Fim Script [+] ")
                break
    elif opcao == "3":
        test = str(input("Criar outra WordList: > [S/N]: ")).upper()
        sair = True
        while(sair):
            if test == "S" or test == "sim":
                nome_wordlist = str(input("Nome da wordlist com extensao .txt !>  "))
                qnt = int(input("Tamanho da wordlist! > "))
                text_frente(qnt,nome_wordlist,qnt_dig)
                sair = str(input("Sair [s]: ")).upper()
                if sair == "S":
                    print("Fim Sciprit [+] ")
                    break
            else:
                print("Fim Script [+] ")
                break
    elif opcao == "4":
        test = str(input("Criar outra WordList: > [S/N]: ")).upper()
        sair = True
        while(sair):
            if test == "S" or test == "sim":
                nome = str(input("Nome: "))
                nome_wordlist = str(input("Nome da wordlist com extensao .txt !>  "))
                qnt = int(input("Tamanho da wordlist! > "))
                Nome_mais_num(nome,qnt,nome_wordlist)
                sair = str(input("Sair [s]: ")).upper()
                if sair == "S":
                    print("Fim Sciprit [+] ")
                    break
            else:
                print("Fim Script [+] ")
                break
    elif opcao == "5":
        test = str(input("Criar outra WordList: > [S/N]: ")).upper()
        sair = True
        while(sair):
            if test == "S" or test == "sim":
                nome = str(input("Nome: "))
                nome_wordlist = str(input("Nome da wordlist com extensao .txt !>  "))
                qnt = int(input("Tamanho da wordlist! > "))
                Num_mais_nome(nome,qnt,nome_wordlist)
                sair = str(input("Sair [s]: ")).upper()
                if sair == "S":
                    print("Fim Sciprit [+] ")
                    break
            else:
                print("Fim Script [+] ")
                break
        
        
        
        
GHP = """
    * #############################################################################
    * ----------- GERADOR DE SENHAS 1.1-----------------------------------------------
    * 
    * Suporta até 10 Digitos !!
    * Opções !
    * [1] = Numero+String = 16215ahwuqw
    * [2] = String+Numero = awwuqw16215
    * [3] = String+Numero Cruzado = 1a2b344
    * [4] = NomePessoa + numero = Osvaldo2534
    * [5] = numero+NOmePessoa = 2534Osvaldo
    *##############################################################################
    *¦¦¦¦¦¦+ ¦¦¦¦¦¦¦¦+     ¦¦¦¦¦¦+¦¦¦¦¦¦+  ¦¦¦¦¦+ ¦¦¦¦¦¦¦+¦¦+  ¦¦+
     ¦¦+--¦¦++--¦¦+--+    ¦¦+----+¦¦+--¦¦+¦¦+--¦¦+¦¦+----+¦¦¦  ¦¦¦
     ¦¦¦¦¦¦++   ¦¦¦       ¦¦¦     ¦¦¦¦¦¦++¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦+¦¦¦¦¦¦¦¦
     ¦¦+--¦¦+   ¦¦¦       ¦¦¦     ¦¦+--¦¦+¦¦+--¦¦¦+----¦¦¦¦¦+--¦¦¦
     ¦¦¦  ¦¦¦   ¦¦¦       +¦¦¦¦¦¦+¦¦¦  ¦¦¦¦¦¦  ¦¦¦¦¦¦¦¦¦¦¦¦¦¦  ¦¦¦
     +-+  +-+   +-+        +-----++-+  +-++-+  +-++------++-+  +-+
    * 
    *Scripter: Osvaldo  Airon;
    *Fuiz!;
    """
print(GHP)
print()
opcao = str(input("Digite a opcao [1] or [2] or [3] or [4]  or [5]: "))
list_qnt_dig = []
list_dig =[]
aux= ''
aux1=''
aux2=''
aux3=''
aux4=''
aux_temp = ''
j = ''
n = ''
f = ''
z = ''
w = ''
x = ''
numbers = ['0','1','2','3','4','5','6','7','8','9']
alfabeto= ['a','b','c','d','e','f','g','h','i','j','l','m','n','o','p','r','s','u','v','x','y','z','k','w']
nome_digitado = ''
num_digitos =[]
if opcao == "1":
    print("--------- Numeros + texto --------")
    qnt_dig = int(input("Digite a quantidade de digitos: "))
    num_digitos = [qnt_dig]
    qnt = int(input("Tamanho da wordlist! >  "))
    Gerador_numero_frente(qnt,"Senha_Salva.txt",num_digitos)
    test =''
    new_WordList(test,opcao)
elif opcao == "2":
    print("-------- Texto + numeros ---------- ")
    qnt_dig = int(input("Digite a quantidade de digitos: "))
    qnt = int(input("Tamanho da wordlist! >  "))
    text_frente(qnt,"Senha_Salva.txt",num_digitos)
    test =''
    new_WordList(test,opcao)
    
elif opcao == "3":
    print("-------- Texto+numeros - 1\s\1\t .. etc ---------- ")
    qnt_dig = int(input("Digite a quantidade de digitos: "))
    qnt = int(input("Tamanho da wordlist! >  "))
    text_frente_cruzado(qnt,"Senha_Salva.txt",num_digitos)
    test =''
    new_WordList(test,opcao)
elif opcao == "4":
    nome = str(input("Nome: "))
    print("-------- NomePEssoa + NUM.. etc ---------- ")
    qnt_dig = int(input("Digite a quantidade de digitos: "))
    qnt = int(input("Tamanho da wordlist! >  "))
    Nome_mais_num(nome,qnt,"Senha_Salva.txt")
    test =''
    new_WordList(test,opcao)
elif opcao == "5":
    nome = str(input("Nome: "))
    print("-------- NomePEssoa + NUM.. etc ---------- ")
    qnt_dig = int(input("Digite a quantidade de digitos: "))
    qnt = int(input("Tamanho da wordlist! >  "))
    Num_mais_nome(nome,qnt,"Senha_Salva.txt")
    test =''
    new_WordList(test,opcao)
    
    
    
else:
    print("Opcao Invalida [Error] !")
