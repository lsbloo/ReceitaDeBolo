#Criptgrafia
#Codigo Morse

def Alfabeto_Morse():
    """
    Funcão que Contém o Código Morse
    Retorno listas alfabeto normal , alfabeto morse
    """
    global Alfabeto_Morse
    global Alfabeto_Normal
    A = ".-"
    B = "-..."
    C = "-.-."
    D = "-.."
    E ="."
    F = "..-."
    G = "--."
    H = "...."
    I = ".."
    J = ".---"
    K = "-.-"
    L = ".-.."
    M = "--"
    N = "-."
    O = "---"
    P = ".--."
    Q = "--.-"
    R = ".-."
    S = "..."
    T = "-"
    U = "..-"
    V = "...-"
    W = ".--"
    X = "-..-"
    Y = "-.--"
    Z = "--.."
    """ A IMPLEMENTAR !
    um = ".----"
    dois= "..---"
    tres= "...--"
    quatro= "....-"
    cinco = "....."
    seis= "-...."
    sete = "--..."
    oito = "---.."
    nove= "----."
    zero = "-----"
    """
    Alfabeto_Morse = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
    Alfabeto_Normal= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    return Alfabeto_Morse , Alfabeto_Normal

GHP = """
    * #############################################################################
    * ----------- CRIPTER DE TEXTO -----------------------------------------------
    * PADRÃO MORSE ; 
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
Alfabeto_Morse()
sair = str(input("Deseja Criptografar [S/N]: !")).upper()
if sair == "S" or sair == "s":
    sair = True
    aux = []
    aux_morse=[]
    cod_morse =[]
    string_morse = ''
    while(sair):
        caract = str(input("[-] Digite o Texto: ")).upper()
        for i in caract:
            aux.append(i)
        for x in aux:
            for k in Alfabeto_Normal:
                if x == k:
                    aux_morse = Alfabeto_Normal.index(k)
                    for z in Alfabeto_Morse:
                        if aux_morse == Alfabeto_Morse.index(z):
                            cod_morse.append(z)


        for x in cod_morse:
            string_morse += x




        print("[+] Texo Criptografado! > ",string_morse)

        sair = str(input("SAIR ! > [S/N]! ")).upper()
        if sair == "S":
            print("END !")
            break
        else:
            string_morse = ''
            aux_morse = []
            cod_morse = []
            aux = []
                            
