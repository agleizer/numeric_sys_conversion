import decimal

def pegaNumIN():
    #print("iniciando pegaNumIN")
    numeroIN = input("Número para conversão (COM CASAS DECIMAIS): ")
    numINlist = strPlista(numeroIN)
    return numINlist

def pegaBase():
    #print("iniciando pegaBase")
    base = input("Informe a base: ")
    if base == "10" or base == "dez" or base == "decimal" or base == "Decimal":
        return 10
    elif base == "8" or base == "oito" or base == "octal" or base == "Octal":
        return 8
    elif base == "2" or base == "dois" or base == "binario" or base == "binário" or base == "Binario" or base == "Binário":
        return 2
    elif base == "16" or base == "hexadecimal" or base == "Hexadecimal" or base == "dezesseis":
        return 16
    #elif base.isnumeric():
        #return int(base)
    else:
        print("Base inválida. Tente novamente.")
        return 0
    
def ehNegativo(lista):
    if lista[0][0] == "-":
        return True
    else:
        return False

def tiraNegativo(lista):
    lista[0].pop(0)
    return lista

def poeNegativo(lista):
    lista[0].insert(0,"-")
    return lista

def paraDec(num, base):
    #print("iniciando paraDec")
    numOUT = 0.0 #var para guardar o numero output em float
    numOUTlist = [[],[]] #lista para output do float
    numINint = num[0]
    numINdec = num[1]
    digitosINT = len(num[0])
    digitosDEC  = len(num[1])
    contINT = 1 #contador para loop INT
    for S in numINint: #loop conversão parte inteira. não pode ser feito direto para lista.
        numOUT += int(S) * base ** (digitosINT - contINT)
        contINT += 1
    contDEC = -1 #contador para loop DEC
    for S in numINdec: #loop conversão parte decimal
        numOUT += int(S) * base ** (contDEC)
        contDEC -= 1
    numOUTlist = strPlista(str(numOUT))
    #print("retorno paraDec:",numOUTlist)
    return numOUTlist

def deDec(num, base):
    #print("iniciando deDec")
    numOUTlist = [[],[]]
    #numINint = num[0]
    numINdec = num[1]
    digitosINT = len(num[0])
    digitosDEC  = len(num[1])
    quociente = int(float(listaPstr(num))) #var quociente para usar no loop INT
    while quociente != 0: #loop para parte inteira
        resto = quociente % base
        numOUTlist[0].insert(0,str(resto)) #inverte a ordem na hora de por na lista
        quociente = quociente // base
    produto = ""
    for i in numINdec: #transforma parte decimal da lista em string
        produto += i
    produto = int(produto) / decimal.Decimal(10**len(produto)) #var produto para usar no loop DEC
    cont = 0 # contador para loop não ser inifnito
    while produto != 0 and cont != 5: #loop para parte decimal
        conta = produto * base
        ptInteira = int(produto * base)
        numOUTlist[1].append(str(ptInteira))
        produto = conta - ptInteira
        cont += 1
    #print("retorno deDec:",numOUTlist)
    return numOUTlist

def deHexa(num):
    #print("iniciando deHexa")
    out = [[],[]]
    for j in range(0,2):
        for i in num[j]:
            if i == "A":
                out[j].append('10')
            elif i == "B":
                out[j].append('11')
            elif i == "C":
                out[j].append('12')
            elif i == "D":
                out[j].append('13')
            elif i == "E":
                out[j].append('14')
            elif i == "F":
                out[j].append('15')
            else:
                out[j].append(i)
    #print("retorno deHexa:",out)
    return out

def paraHexa(num):
    #print("iniciando paraHexa")
    out = [[],[]]
    for j in range(0,2):
        for i in num[j]:
            if i == "10":
                out[j].append('A')
            elif i == "11":
                out[j].append('B')
            elif i == "12":
                out[j].append('C')
            elif i == "13":
                out[j].append('D')
            elif i == "14":
                out[j].append('E')
            elif i == "15":
                out[j].append('F')
            else:
                out[j].append(i)
    #print("retorno paraHexa:",out)
    return out

def strPlista(entrada):
    #print("iniciando strPlista")
    lista = [[],[]]
    entrada = str(entrada)
    strIN = entrada.split(".") #separa parte inteira da parte decimal
    strINint = strIN[0]
    strINdec = strIN[1]
    for i in strINint:
        lista[0].append(i)
    for i in strINdec:
        lista[1].append(i)
    #print("retorno strPlista:",lista)
    return lista

def listaPstr(lista):
    #print("iniciando listaPstr")
    numOUT = ""
    for i in lista[0]:
        numOUT = numOUT + str(i)
    numOUT = numOUT + "."
    if lista[1] == []:
        numOUT += "00"
    for i in lista[1]:
        numOUT = numOUT + str(i)
    #print("retorno listaPstr:",numOUT)
    return numOUT

def main():
    print("\nCONVERSOR DE SISTEMAS NUMÉRICOS v3")
    num = pegaNumIN()
    print("\nBase em que o número está.")
    baseIN = pegaBase()
    while baseIN == 0:
        baseIN = pegaBase()
    print("\nBase para conversão.")
    baseOUT = pegaBase()
    while baseOUT == 0:
        baseOUT = pegaBase()
    negativo = False #variável p armazenar se o número de input era negativo
    if ehNegativo(num): #checa se a lista começa com -. se sim, retira o -
        num = tiraNegativo(num)
        negativo = True
    if baseIN == 16: #se input for em hexa, converter os caracteres A-F -> 10-15
        num = deHexa(num)
    num10inter = paraDec(num,baseIN) #converter o numero de input para base 10
    numConv = deDec(num10inter,baseOUT) #converter da base 10 para base OUTPUT
    if negativo: #se o numero de input era negativo
        numConv = poeNegativo(numConv) #colocamos - no inicio da lista de output
    if baseOUT == 16: #se output for em hexa
        print("\n")
        print(listaPstr(paraHexa(numConv))) #converter 10-15 para A-F, converter lista para string
    else:
        print("\n")
        print(listaPstr(numConv)) #converter lista para string

#testes - ignorar
#pegaNumIN()
#strPlista("105135.00")
#listaPstr([['1', '0', '5', '1', '3', '5'], ['0', '0']])
#paraDec([['1', '0', '5', '1', '3', '5'], ['0', '0']],8)
#deHexa([['8', 'A', '5', 'D'], ['0', '0']])
#paraHexa([['8', '10', '5', '13'], ['0', '0']])
#paraDec(deHexa([['8', 'A', '5', 'D'], ['0', '0']]),16) #IMPORTANTE!!!
#deDec([['3', '5', '4', '2', '1'], ['6', '7']],2)
#paraHexa(deDec([['3', '5', '4', '2', '1'], ['6', '7']],16))
#print(ehNegativo(strPlista("-100.00")))

main()

