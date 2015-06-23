# -*- coding: utf-8 -*-
# Comunicacao com a placa agilent U2531A
#
# UFC - Universidade de Federal do Ceará
#
# Responsáveis:
# Felipe Bandeira da Silva
# Francisco Alexander 
#

from __future__ import division

import platform

#if platform.system() == 'Windows':
#    import visa
#else:
#    import visa_linux_emulation as visa

try:
    import visa
except:
    # Durante o processo de instalação normal usando o NSIS, o path do windows
    # não estava atualizado com o Python, portanto não era possível, durante a instalação,
    # a execução do pip para instalar o "pyvisa" que requer por natureza, várias
    # dependências que são simplesmene tratadas pelo pip. Portanto para a primeira
    # utilização do programa é necessário a utilização da internet.
    #
    # Para que tudo funcione corretamente e necessario pyvisa 1.4
    #import pip
    #pip.main(['install', 'pyvisa'])

    import subprocess
    print u"aviso: instalando o PyVISA 1.4"
    subprocess.call(['pip', 'install', 'PyVISA==1.4'])
    print u"aviso: instalacao finalizada"
    import visa

import matplotlib.pyplot as plt
from time import sleep, time, asctime, localtime
import numpy as np


###############################################################################
# Constantes para correçao. As mesmas usadas pelo programa feito no LabView
###############################################################################
FATOR_CORRECAO_TENSAO = 100
FATOR_CORRECAO_CORRENTE = 2.71

# 0 - nao mostra as mensagens
# 1 - mostras as mensagens para debug
DEBUG = 0


# um pequeno pulso inicial é visto no inicio da
# aquisição, puro ruido. Para que o sinal seja
# visualizado corretamento foi necessário aumentar
# o número de aquisições. Isso implica em uma
# aquisição mais demorada.

#QUANTIDADE_PONTOS = 50000
QUANTIDADE_PONTOS = 800000

###############################################################################


# testBit() returns a nonzero result, 2**offset, if the bit at 'offset' is one.
def testBit(int_type, offset):
    mask = 1 << offset
    return(int_type & mask)

# setBit() returns an integer with the bit at 'offset' set to 1.
def setBit(int_type, offset):
    mask = 1 << offset
    return(int_type | mask)

# clearBit() returns an integer with the bit at 'offset' cleared.
def clearBit(int_type, offset):
    mask = ~(1 << offset)
    return(int_type & mask)

# toggleBit() returns an integer with the bit at 'offset' inverted, 0 -> 1 and 1 -> 0.
def toggleBit(int_type, offset):
    mask = 1 << offset
    return(int_type ^ mask)


def lerEndian(data):  
    """
    Converte um sequencia de dados em valores de 2 bytes
    A sequencia de entrada é dada no formato little-endian
    com entrada do 13 bit para o carry.
    Entrada:
        data = string pura com informacoes do bloco de bytes
    Saída:
        t = tamanho do vetor de bytes
        v = valores em um vetor
    """
    raw = data[10:]
    
    valores = []    
    passo = 0
    for i in raw:
        if passo == 0:
            lsb = i
            passo = 1
        elif passo == 1:
            msb = i
            passo = 0
            num = ((ord(msb)<<8)+(ord(lsb)))>>2
            #print hex(num)    
            valores.append(num)
        
    return [len(valores), valores]

def ler2Endian(data):
    """
    Ler um bloco de bytes composto por duas leitura simultaneas do canal.
    """
    
    raw = data[10:]
    A = []
    B = []
    passo = 0
    
    for i in raw:
        if passo == 0:
            lsb = i
            passo = 1
        elif passo == 1:
            msb = i
            passo = 2
            A.append(((ord(msb)<<8)+(ord(lsb)))>>2)
        elif passo == 2:
            lsb = i
            passo = 3
        elif passo == 3:
            msb = i
            passo = 0
            B.append(((ord(msb)<<8)+(ord(lsb)))>>2)
        
    return [len(A), A, B]
    
def convBIP(raw, range_ad=10, resolution=14):
    v = []
    for i in raw:
        v.append( (2*i)/(2**resolution)  * range_ad )
    return v
    
def convUNI(raw, range_ad=10, resolution=14):
    v = []
    for i in raw:
        # se o 13 bit do byte for 1 então o número é "negativo"
        # a conversão unipolar é dada por
        # MAX = 1FFF
        # MAX/2 = 0000
        # 0 = 2000
        if testBit(i, 13) > 0:
            valor = clearBit(i, 13) - (2**14)/2
            v.append( (valor/(2**resolution) + 0.5)*range_ad )
        else:
            v.append( (i/(2**resolution) + 0.5)*range_ad )
    return v


def lerTensaoCorrente(ag):
    """
    Faz a leitura de dois canais de forma simultanea
    Canal 101(corrente) e 102(tensão)
    """
    
    # reseta a placa a de aquisição
    ag.write("*CLS")
    ag.write("*RST")
    
    ag.write("ROUT:ENAB 0,(@103, 104)") # desabilita os canais 103 e 104
    ag.write("ROUT:ENAB 1,(@101, 102)") # habilita os canais 101 e 102
    ag.write("ROUT:CHAN:RANG 10,(@101, 102)")   # coloca no mesmo nivel que o programa da National
    ag.write("ROUT:CHAN:POL UNIP,(@101, 102)")  # unipolar
    ag.write("ACQ:SRAT 2000000")    # frequencia de amostragem
    #ag.write("ACQ:POIN 2000000")    
    #ag.write("ACQ:POIN 50000")  # número de pontos para aquisição
    ag.write("ACQ:POIN %d" % QUANTIDADE_PONTOS)
        
    ####################
    # inicia aquisicao #
    ####################
    ag.write("DIG")

    disparaTensao(ag)

    #ag.write("DIG")
    
    while True:
        ag.write("WAV:COMP?")
        if ag.read() == 'YES':
            break
        sleep(0.2)  # espera um tempo até que amostra fique pronta

    # Uma pequena mudança no capacitor do primeiro 555
    # faz com que o set e reset necessitem de um tempo
    # maior para que ambos acontecam.
    sleep(.2)

    retiraTensao(ag)
    
    ag.write("WAV:DATA?")
    dados = ag.read()
    
    t, I, V = ler2Endian(dados)
      
    V = convUNI(V, 10)
    I = convUNI(I, 10)
        
    return [dados, V, I]
   
def lerTensao(ag):
    """
    Ler apenas o canal de tensão da fonte. Canal 102
    Com toda a sequencia de acionamento do set e reset.
    """
    # reset
    ag.write("*CLS")
    ag.write("*RST")
    
    # inicia a leitura do canal 102 tensao
    ag.write("ROUT:ENAB 0,(@103, 101, 104)")
    ag.write("ROUT:ENAB 1,(@102)")
    ag.write("ROUT:CHAN:RANG 10,(@102)")        # coloca no mesmo nivel que o programa da National
    ag.write("ROUT:CHAN:POL UNIP,(@102)")
    ag.write("ACQ:SRAT 2000000")
    #ag.write("ACQ:POIN 2000000")    
    #ag.write("ACQ:POIN 50000")

    # um pequeno pulso inicial é visto no inicio da
    # aquisição, puro ruido. Para que o sinal seja
    # visualizado corretamento foi necessário aumentar
    # o número de aquisições. Isso implica em uma
    # aquisição mais demorada.
    ag.write("ACQ:POIN %d" % (QUANTIDADE_PONTOS))
        
    # inicia aquisicao
    ag.write("DIG")

    disparaTensao(ag)
    
    while True:
        ag.write("WAV:COMP?")
        if ag.read() == 'YES':
            break
        sleep(0.5)
    
    ag.write("WAV:DATA?")
    dados = ag.read()

    sleep(.2)

    retiraTensao(ag)
    
    #print dados
    
    t, R = lerEndian(dados)    
    V = convUNI(R, 10)
    plt.grid()
    plt.plot(range(0, t), V)
    plt.show()
    
    return t, V


def lerCorrente(ag):
    """
    Ler apenas o canal de corrente da fonte. Canal 101
    Com toda a sequencia de acionamento do set e reset.
    """
    # reset
    ag.write("*CLS")
    ag.write("*RST")
    
    # inicia a leitura do canal 101 corrente
    ag.write("ROUT:ENAB 0,(@103, 102, 104)")
    ag.write("ROUT:ENAB 1,(@101)")
    ag.write("ROUT:CHAN:RANG 10,(@101)")
    ag.write("ROUT:CHAN:POL UNIP,(@101)")
    ag.write("ACQ:SRAT 2000000")
    ag.write("ACQ:POIN 2000000")    
        
    # inicia aquisicao
    ag.write("DIG")

    disparaTensao(ag)
    
    while True:
        ag.write("WAV:COMP?")
        if ag.read() == 'YES':
            break
        sleep(0.5)
    
    ag.write("WAV:DATA?")
    dados = ag.read()

    sleep(.2)
    retiraTensao(ag)
    
    #print dados
    
    t, R = lerEndian(dados)    
    V = convUNI(R, 10)
    plt.grid()
    plt.plot(range(0, t), V)
    plt.show()
    
    return t, V


    
def lerCanal103(ag):
    """
    Este canal foi usado para os testes iniciais da conversão 
    do análogico digital. Não sendo mais necessário. 
    As funçoes para leitura de tensão e corrente são identicas
    a esta funçao. Mudando apenas o canal.
    """
    # reset
    ag.write("*CLS")
    ag.write("*RST")
    
    # inicia a leitura do canal 103
    ag.write("ROUT:ENAB 0,(@101, 102, 104)")
    ag.write("ROUT:ENAB 1,(@103)")
    ag.write("ROUT:CHAN:RANG 10,(@103)")
    #ag.write("ROUT:CHAN:POL BIP,(@103)")
    ag.write("ROUT:CHAN:POL UNIP,(@103)")
    ag.write("ACQ:SRAT 2000000")
    ag.write("ACQ:POIN 2000000")    
        
    # inicia aquisicao
    ag.write("DIG")
    # espera o fim

    disparaTensao(ag)
    
    while True:
        ag.write("WAV:COMP?")
        if ag.read() == 'YES':
            break
        sleep(0.1)
    
    ag.write("WAV:DATA?")
    dados = ag.read()

    sleep(.2)
    retiraTensao(ag)
    
    #print dados
    
    t, R = lerEndian(dados)    
    V = convUNI(R)
    plt.grid()
    plt.plot(range(0, t), V)
    
    return t, V
    
def disparaTensao(ag):
    """
    Envia um pulso de alta tensão para o sistema de aterramento.
    Acionando para isto o primeiro 555.
    Os pulso não deve ser enviando em um curto intervalo de tempo
    já que a fonte não foi projetada para tal situaçao. 
    Portanto deve-se tormar cuidado no acionamento sequencia.
    SET - Pino 68 na placa U2901-60602
    RESET - Pino 34 na placa U2901-60602
    """
    ag.write("CONF:DIG:DIR OUTP,(@501)")
    ag.write("SOUR:DIG:DATA 1,(@501)")
    
    return 0
    
def retiraTensao(ag):
    """
    Reseta a fonte. Habilitando a mesma para um novo envio 
    de um pulso de alta tensão.
    """
    ag.write("CONF:DIG:DIR OUTP,(@501)")
    ag.write("SOUR:DIG:DATA 0,(@501)")  # desabilita o set
    sleep(0.1)                          # espera um tempo para resetar
    ag.write("SOUR:DIG:DATA 2,(@501)")  # reseta a fonte
    sleep(0.1)                          # espera um tempo para entrar em repouso
    ag.write("SOUR:DIG:DATA 0,(@501)")  # entra em repouso
        
    return 0    
  

def pltTensaoCorrente(V, I):
    t1 = np.arange(0, len(V))
    plt.figure(1)
    plt.title("Leitura do U2531A")
    plt.subplot(211)
    plt.plot(t1, V)
    plt.subplot(212)
    plt.plot(t1, I)
    plt.show()    
    
    
def aplicaCorrecoes(V, I):
    V = np.array(V)
    V = FATOR_CORRECAO_TENSAO * V
    I = np.array(I)
    I = FATOR_CORRECAO_CORRENTE * I
    
    return [V, I]
    
def sequenciaAquisicoes(ag, quantidade, local="C:\\Temp", rotulo = '0'):
    """
    Faz um aquisiçao sequencial dos canais de tensão e corrente.
    ag = objeto usada para o controle da placa
    """    
    
    print "Iniciando aquisicao sequencial"
    print "Equipamento = ", ag
    print "quantidade = ", quantidade    
    print "Tempo de inicio = ", asctime()
    
    tempoInicio = time()
    contagem = quantidade
    
    plt.figure(1)
    
    while quantidade > 0:        
        print "Atual = ", quantidade
        tempoIndividual = time()
        
        # inicia aquisição
        raw, V, I = lerTensaoCorrente(ag)
        V, I = aplicaCorrecoes(V, I)

        # não é uma boa ideia plotar desta forma
        #pltTensaoCorrente(V, I)

        plt.subplot(211)
        plt.plot(np.arange(0, len(V)), V)
        
        plt.subplot(212)
        plt.plot(np.arange(0, len(I)), I)
        
        salvaTensaoTXT(local, rotulo, contagem-quantidade+1, V)
        salvaCorrenteTXT(local, rotulo, contagem-quantidade+1, I)
                
        print "Individual = ", time()-tempoIndividual
        quantidade -=1
        
    total = time()-tempoInicio
    print 'Completo em [seg]: ', total
    plt.show()
    return 0

def salvaTensaoTXT(local, rotulo, posicao, V):
    """
    Salva o vetor tensão em um arquivo com nome formatado para isso
    """
    nomeCompleto = local+"\\"+rotulo+"V"+str(posicao)+".txt"
    return salvaTXT(nomeCompleto, V)
    
def salvaCorrenteTXT(local, rotulo, posicao, I):
    """
    Salva o vetor corrente em um arquivo com nome formatado para isso
    """    
    nomeCompleto = local+"\\"+rotulo+"I"+str(posicao)+".txt"
    return salvaTXT(nomeCompleto, I)    

def salvaTXT(caminhoCompleto, vetor):
    """
    Salva em um arquivo txt os valores de um vetor
    onde a primeira coluna informa o indice e a segunda
    coluna informa o valor para o indice.
    """
    try:
        arquivo = open(caminhoCompleto, 'w')
    except:
        print 'erro: nao foi possivel escrever no arquivo'
        print '    : ', caminhoCompleto
        return -1
    
    #for i in range(len(vetor)):
    #    string = "%d %f\n" % (i, float(vetor[i]))
    #    arquivo.write(string)

    for i in vetor:
        arquivo.write(i)
        
    arquivo.close()
        
    # escrita finalizada com sucesso
    return 0

def buscaAgilent():
    """
    Busca o equipamento conectado a porta usb do computador
    Retornando o objeto a ser usado pelas funções de controle
    da placa de aquisiçao da agilent.
    """
   
    listaInstrumentos = visa.get_instruments_list() # adquiri a lista de equipamentos conectados ao computador
    listaAgilent = listaInstrumentos[0]     # pega o primeiro equipamento
    
    print 'Lista de instrumentos:'
    print listaAgilent      # espera-se que o equipamento seja da agilent
    
    ag = visa.instrument(listaAgilent)  # cria um objeto a ser manipulado e passado para as outras funções
    
    identificacao = ag.ask("*IDN?")
    print identificacao
    
    return ag
  

###############################################################################
# MAIN                                                                        #         
###############################################################################
if __name__ == '__main__':  
    print 'Agilente U3125A'
    
    ag = buscaAgilent()
     
    ##############################
    # leitura de apenas um canal #
    ##############################
    #lerCanal103(ag)   
    #lerTensao(ag)
    #lerCorrente(ag)
     
    ##########################
    # leitura de dois canais #
    ##########################
    raw, V, I = lerTensaoCorrente(ag)
    V, I = aplicaCorrecoes(V, I)
    pltTensaoCorrente(V, I)
    
    #########################
    # Aquisiçoes sequencial #
    #########################  
    # 60 aquisições
    # local onde é salvo "C:\Temp"
    #sequenciaAquisicoes(ag, 10)
    
    