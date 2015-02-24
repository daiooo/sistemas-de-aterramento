# -*- coding: utf-8 -*-
# Controle das ações do GUI principal
#
# UFC - Universidade de Federal do Ceará
#
# Responsáveis:
# Felipe Bandeira da Silva
# Francisco Alexander
#

from __future__ import division

from PyQt4 import QtCore, QtGui
import sys
from time import time, localtime, sleep
import os  # implementa a manipulação de diretorios e arquivos com o python
import re  # leitura de padrões em determinadas strings
import platform

from numpy import arange
from scipy import genfromtxt
import matplotlib.pyplot as plt
from scipy.io import loadmat, savemat

import agilent_u2531a
import projATT_functions as pat

import numpy as np


# Tempo estimado para cada amostra
TEMPO_ESTIMADO = 5.6

# Modo de funcionamento da Fonte:
# A fonte possui dois modos de ligação interna para identificação
# de uma topologia de aterramento. Serão aqui chamados de modo 1 e
# modo 2.
#
# O modo 1 é conhecido por nao utilizar a haste de retorno e portanto
# é necessário apenas uma haste auxiliar.
#
# O modo 2 utiliza de duas hastes, uma chamada de haste de tensão e
# outra chamada de haste de corrente.
#
# 29 jan 15:
# O modo escolhido dentro do laboratório será o exato e portanto
# as informações ligadas ao modo 2 deve ser retiradas, são elas,
# - figura mostrando a segunda haste
# - informações sobre o número aproximado de hastes

# MODO = 'duas_hastes'
MODO = 'haste_auxiliar'


if platform.system() == 'Windows':
    print 'aviso: plataforma, Windows'
    _separador = "\\"
elif platform.system() == 'Linux':
    print 'aviso: plataforma, Linux'
    _separador = '/'
else:
    print u"ERRO: plataforma não suportada pelo software"

# necessário para o pyqt4 funcionar
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

# necessário para o pyqt4 funcionar
try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

# chamada da classe que define os objetos na tela
from sistemaAquisicao_python import Ui_MainWindow


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    """
    Rotina principal que controla as ações que são executadas
    na janela principal do programa agilent U2531A.
    Aqui toda alteração feita usando o qtcreator não influência
    no funcionamento dos componentes já implementados.
    """
    _window_list = []

    def __init__(self):
        # necessário para a inicialização
        super(MainWindow, self).__init__()
        MainWindow._window_list.append(self)
        self.setupUi(self)

        #self.screen_aumento()
        #self.showFullScreen()

        if MODO == 'haste_auxiliar':
            self.label_5.hide()
            self.label_7.hide()
            self.label_22.hide()
            self.label_23.hide()
            self.label_24.hide()
            self.label_29.hide()

            # nunca mais fazer isso
            #self.label_17.setPixmap(QtGui.QPixmap(_fromUtf8("figuras/esquema_ligacao_modo1.svg")))

        '''
        Inicia as definições de cada ação, para cada componente do gui
        '''

        self.actionSair.triggered.connect(self.close)  # fecha o programa
        self.actionSobre_o_Software.triggered.connect(self.sobreSoftware)  # sobre o software
        self.actionLamotriz.triggered.connect(self.lamotriz)  # sobre o lamotriz
        self.actionO_Projeto.triggered.connect(self.sobreProjeto)  # sobre o projeto

        self.actionAnalisar.triggered.connect(self.analisar)  # botao analisar na barra de tarefas
        self.actionAnalisar_Amostras.triggered.connect(self.pos_analise)

        self.actionTreinar.triggered.connect(self.treinar_modelo)

        # atualiza a mensagem inicial do status bar
        self.statusBar().showMessage("Parado")

        # ações do usuario, via botoes
        self.connect(self.pushAnalisar, QtCore.SIGNAL("clicked()"), self.analisar)  # botao analisar na gui
        self.connect(self.pushCancelar, QtCore.SIGNAL("clicked()"), self.cancelar)  # botão treinar


        # verifica se a placa u2531a esta conectada ao computador
        # se sim atualiza as variaveis relacionadas.
        self.actionConectar.triggered.connect(self.conectar)

        # carrega a area de trabalho, onde sera usada para salvar todos os dados
        # das medições em txt
        self.actionAbrir.triggered.connect(self.abrir)

        self.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.abrir)

        # verifica se é necessário ou nao plotar o grafico
        self.connect(self.checkBox, QtCore.SIGNAL("clicked()"), self.checkBoxPlotGrafico)
        self.flagPlotGrafico = 0

        self.actionPlot_V_I_transiente.triggered.connect(self.plot_mat_especifico)
        self.actionPlot_V_I_raw.triggered.connect(self.plot_mat_raw)
        self.spinBox.valueChanged.connect(self.atualizaTempoEstimado)

        # o usário deve seleciona uma area de trabalho primeiro
        # pathTrabalho = local onde os arquivos estão localizados
        # areaTrabalho = local onde as pastas serao colocadas para cada topologia do aterramento testada
        #
        # a se verificar:
        # Salvar os arquivos no formato TXT gera arquivos muito grandes. E em poucas medições
        # é possivel ter Gbytes no disco.
        # No momento uma medição de tensão ou corrente consome aproximadamente 800kb para uma
        # amostra de 5e4.
        if not self.lerAreaTrabalhoTXT():
            self.areaTrabalho = self.areaTrabalhoTXT
            self.atualizaStatusAreaTrabalho()
        else:
            self.areaTrabalho = 0

        self.pathTrabalho = 0
        # placa u2531a deve ser encontrada
        self.ag = 0

        self.atualizaTempoEstimado()

        self.fCancelar = 0
        self.fInicioProcesso = 0

        self.actionCANCELAR.triggered.connect(self.cancelar)

        # É necessário treinar o modelo
        self.ver_treinar_modelo()

    def ver_treinar_modelo(self):
        '''
        Verifica se existe a necessidade de treinar o modelo, caso sim treina o modelo.
        Criando tres arquivos no diretorio corrente
        :return:
        '''

        try:
            arq = open('projATT_strfore.pckl', 'r')
            print u'aviso: ver_treinar_modelo: modelo já treinado'
        except:
            print u'aviso: ver_treinar_modelo: é necessário treinar o modelo'
            self.treinar_modelo()


    def atualizaTempoEstimado(self):
        self.label_28.setText("%f" % (TEMPO_ESTIMADO*int(self.spinBox.value())))

    def abrir(self):
        self.areaTrabalho = QtGui.QFileDialog.getExistingDirectory(self, "Area de Trabalho")
        if self.areaTrabalho:
            print self.areaTrabalho
            self.salvaAreaTrabalhoTXT()
            self.atualizaStatusAreaTrabalho()
        else:
            print u'abrir: erro: nenhuma área de trabalho selecionada'
            self.statusBar().showMessage(u"Nenhuma área de trabalho selecionada")

    def atualizaStatusAreaTrabalho(self):
        self.statusBar().showMessage(u"Área de trabalho: %s" % (self.areaTrabalho))

        #if len(str(self.areaTrabalho)) > 40:
        #    self.label_9.setText(str(self.areaTrabalho)[:8]+' [...] '+str(self.areaTrabalho)[-35:])
        #else:
        #    self.label_9.setText(str(self.areaTrabalho))
        self.label_9.setText(str(self.areaTrabalho))

    def sobreSoftware(self):
        QtGui.QMessageBox.about(self, "Sobre o Projeto",
                                u"Comunicação entre a placa U2531A")

    def lamotriz(self):
        QtGui.QMessageBox.about(self, "Lamotriz",
                                u"O curso de graduação em Engenharia Elétrica da Universidade Federal do Ceará (UFC) foi criado em 19 de julho de 1974. O departamento de Engenharia Elétrica (DEE) foi criado em 21 de julho de 1983, atualmente o curso de graduação em Engenharia Elétrica da UFC conta com 600 alunos e tem conceito máximo (5) na avaliação do MEC. A pós-graduação em Engenharia Elétrica foi criada em 1994 com a implantação do mestrado que já conta com aproximadamente 100 dissertações defendidas. Em 2007 foi iniciado o programa de doutorado. O DEE-UFC já em 1992 implanta uma disciplina opcional no curso de graduação intitulada Introdução à Conservação de Energia tornando-se a primeira universidade brasileira a abordar o tema da conservação de energia em sua estrutura curricular. Neste cenário, o programa de eficiência no consumo de energia elétrica da UFC foi criado, em janeiro 2003, a partir do convênio entre a ELETROBRÁS e a UFC visando à eficiência no consumo e o estímulo ao uso racional de energia elétrica nos prédios da UFC. A idéia do Laboratório de Eficiência Energética em Sistemas Motrizes - LAMOTRIZ do DEE da Universidade Federal do Ceará surge no mesmo ano de 2003, a partir de um desafio do Dr. George Alves Soares do departamento de desenvolvimento de projetos especiais da ELETROBRÁS, no sentido de se desenvolver um laboratório no qual se pudesse simular e ensaiar cargas industriais, o objetivo é a analise do comportamento destas cargas em face de eficiência energética, sendo pesquisadas novas técnicas de acionamento. Em Março de 2006 o LAMOTRIZ foi inaugurado e no mesmo ano já produz as primeiras dissertações de mestrado. ")

    def sobreProjeto(self):
        QtGui.QMessageBox.about(self, "Lamotriz",
                                u"nada ainda")

    def analisar(self):
        """
        Inicia a analise do terreno:
        - inicia a area de trabalho (pasta)
        - busca a placa, se a mesma não foi inicializada
        - manda os comandos necessários para a leitura de tensão e corrente
        - salva individualmente cada amostra de tensao e corrente (vetores)
        - aplica os algoritmos do Alexandre para a classificação do terreno
        - se o plot foi habilitado, mostra todas as amostras em um unico grafico.
        """

        # desabilita a entrada multipla
        self.disconnect(self.pushAnalisar, QtCore.SIGNAL("clicked()"), self.analisar)  # botao analisar na gui

        try:

            if not self.areaTrabalho:
                QtGui.QMessageBox.warning(self, "Erro",
                                          u"Selecione a área de trabalho para continuar")
                self.abrir()

                if not self.areaTrabalho:
                    return

            if self.ag == 0:
                if self.conectar() == -1:
                    return -1

            if self.ag:
                print u"Iniciando analise..."
                print u"Equipamento: ", self.ag

                dia = localtime()
                self.pathTrabalho = "%s\\%s_%02d%02d%02d" % (self.areaTrabalho, str(self.lineEdit.text()), dia.tm_mday, dia.tm_mon, dia.tm_year)

                # verificando o diretorio, cria se não existir
                try:
                    os.mkdir(self.pathTrabalho)
                except:
                    print u"aviso: pasta já existe"

                self.progressBar.setEnabled(True)
                self.label_4.setText(u'Injeção de Corrente')

                tempoInicio = time()
                quantidade = self.spinBox.value()

                self.label_28.setText("%d" % (TEMPO_ESTIMADO*int(self.spinBox.value())))

                contagem = quantidade

                V1 = np.zeros([5e4,1])
                I1 = np.zeros([5e4,1])

                V1_puro = np.zeros([8e5,1])
                I1_puro = np.zeros([8e5,1])

                M_ind_maxI_toSave = np.zeros(1)
                M_ind_maxV_toSave = np.zeros(1)

                str_fCancelar = ''

                self.fInicioProcesso = 1

                while quantidade > 0:
                    # evita que o programa apresente
                    # "não respondendo" na janela do windows
                    # Durante o processo de analise as funções do PyQt
                    # precisam ser atendidas pelo software. Para tanto
                    # é necessário chamar o processEvents(). Se não a
                    # messagem "não respondendo" irá aparecer na janela.

                    if self.fCancelar:
                        self.fCancelar = 0
                        str_fCancelar = 'cancelado'
                        break

                    QtGui.qApp.processEvents()

                    print u"Atual = ", quantidade
                    tempoIndividual = time()

                    # inicia aquisição
                    raw, V, I = agilent_u2531a.lerTensaoCorrente(self.ag)
                    V, I = agilent_u2531a.aplicaCorrecoes(V, I)
                    V = np.array(V)
                    I = np.array(I)

                    V1_trans,I1_trans, ind_maxI_toSave,ind_maxV_toSave = pat.extract_transient(V,I)

                    V1 = np.append(V1,V1_trans,axis=1)
                    I1 = np.append(I1,I1_trans,axis=1)

                    V1_puro = np.append(V1_puro, np.array(V,ndmin=2).transpose(),axis=1)
                    I1_puro = np.append(I1_puro, np.array(I,ndmin=2).transpose(),axis=1)

                    M_ind_maxV_toSave = np.append(M_ind_maxV_toSave,ind_maxV_toSave)
                    M_ind_maxI_toSave = np.append(M_ind_maxI_toSave,ind_maxI_toSave)

                    print "V1: ", V1
                    print "V1_trans",V1_trans
                    print "V",V
                    print "ind_V", M_ind_maxV_toSave
                    print "ind_I", M_ind_maxI_toSave

                    self.progressBar.setValue((100. / contagem) * (contagem - quantidade + 1))

                    print "Individual = ", time() - tempoIndividual
                    quantidade -= 1

                self.fInicioProcesso = 0

                V1 = np.delete(V1,0,1)
                I1 = np.delete(I1,0,1)
                V1_puro = np.delete(V1_puro,0,1)
                I1_puro = np.delete(I1_puro,0,1)
                M_ind_maxV_toSave = np.delete(M_ind_maxV_toSave,0)
                M_ind_maxI_toSave = np.delete(M_ind_maxI_toSave,0)

                if str_fCancelar:
                    print u'Cancelado'
                    self.statusBar().showMessage(u'Cancelado')

                savemat(self.pathTrabalho+'\\'+str(self.lineEdit.text())+str(self.lineEdit_2.text()+str_fCancelar),{'V1':V1,'I1':I1,'V1_raw':V1_puro,'I1_raw':I1_puro,'IndI':M_ind_maxI_toSave,'IndV':M_ind_maxV_toSave})

                total = time() - tempoInicio
                print u'Completo em [seg]: ', total

                self.label_12.setText(str(total))

                self.progressBar.setValue(100)

                QtGui.qApp.processEvents()

                self.label_4.setText(u'Analisando')

                try:
                    tipo, num_exato = pat.returnNumberRods(V1, I1)
                except:
                    tipo = 'erro'
                    num_exato = 'erro'

                if tipo[0] == 0:
                    msgHastes = "1 a 2 hastes"
                elif tipo[0] == 1:
                    msgHastes = "3 a 4 hastes"
                elif tipo[0] == 'erro':
                    msgHastes = 'ERRO'
                else:
                    msgHastes = "Nenhuma haste, %s" % (str(tipo))

                self.label_7.setText(msgHastes)
                self.label_31.setText(str(num_exato))

                self.label_4.setText(u'Fim')
                self.progressBar.setEnabled(False)

                if self.flagPlotGrafico:
                    self.plot_grafico_atual(V1, I1)

                print u"Fim do processo de análise"

                self.connect(self.pushAnalisar, QtCore.SIGNAL("clicked()"), self.analisar)  # botao analisar na gui
            else:
                self.connect(self.pushAnalisar, QtCore.SIGNAL("clicked()"), self.analisar)  # botao analisar na gui
                return -1
        except:
            self.connect(self.pushAnalisar, QtCore.SIGNAL("clicked()"), self.analisar)  # botao analisar na gui

    def plot_grafico_atual(self, V1, I1):
        plt.subplot(211)
        plt.xlabel(u'Amostra')
        plt.ylabel(u'Tensão')
        plt.plot(V1)

        plt.subplot(212)
        plt.xlabel(u'Amostra')
        plt.ylabel(u'Corrente')
        plt.plot(I1)

        plt.show()

    def plot_mat_especifico(self):
        arquivo = str(QtGui.QFileDialog.getOpenFileName(self, u'Plot gráfico, TRANSIENTE', self.areaTrabalho))
        print arquivo

        m = u"Carregando o plot..."

        self.statusBar().showMessage(m)
        self.label_4.setText(m)

        data = loadmat(arquivo)
        V1 = data['V1'].squeeze()
        I1 = data['I1'].squeeze()

        m = u"Fim do carregar plot"
        self.statusBar().showMessage(m)
        self.label_4.setText(m)

        self.plot_grafico_atual(V1, I1)

    def plot_mat_raw(self):
        arquivo = str(QtGui.QFileDialog.getOpenFileName(self, u'Plot gráfico, RAW', self.areaTrabalho))
        print arquivo

        m = u"Carregando o plot..."

        self.statusBar().showMessage(m)
        self.label_4.setText(m)

        data = loadmat(arquivo)
        V1 = data['V1_raw'].squeeze()
        I1 = data['I1_raw'].squeeze()

        m = u"Fim do carregar plot"
        self.statusBar().showMessage(m)
        self.label_4.setText(m)

        self.plot_grafico_atual(V1, I1)

    def conectar(self):
        self.statusBar().showMessage(u"Buscando a placa da agilent...")
        self.ag = 0
        try:
            self.ag = agilent_u2531a.buscaAgilent()
            print self.ag
            self.statusBar().showMessage(u"Placa da Agilent encontrada: %s" % (self.ag))
        except:
            self.statusBar().showMessage(u"ERRO: a placa não foi encontrada")
            QtGui.QMessageBox.warning(self, u"Falha na busca",
                                      u"A busca pela placa U2531A falhou. A placa está conectada a usb? e corretamente energizada?")
            return -1

        return 0

    def nadaImplementado(self):
        QtGui.QMessageBox.about(self, "Lamotriz",
                                u"nada ainda")

    def checkBoxPlotGrafico(self):
        """
        Verifica se o gráfico será habilitado no final da aquisição
        """
        self.flagPlotGrafico = ~self.flagPlotGrafico
        print "Plot grafico: ", self.flagPlotGrafico

    def plotGrafico(self):
        """
        A ideia é plotar o gráfico em uma janela a parte.
        Entretando um erro ocorre quando da execução do pyqt e o matplotlib
        por isso essa rotina só deve ser executada no final de cada comando.
        Como exemplo, ela só deve ser executada no final da aquisição
        dos dados por parte da placa da agilent.
        """
        if self.pathTrabalho:
            conteudoPasta = os.listdir(self.pathTrabalho)
            print u'plotGrafico: conteudo da pasta, ', conteudoPasta
            self.statusBar().showMessage(u'Lendo o conteudo da pasta')

            padraoStrCorrente = re.compile(r'\d\I')
            padraoStrTensao = re.compile(r'\d\V')

            # cria a figura que será utilizada para plotar
            # tensão e corrente na mesma janela
            plt.figure(1)

            self.progressBar.setEnabled(True)
            self.label_4.setText(u'Lendo Graficos')

            cont = 0
            pastaComDados = 0
            for arq in conteudoPasta:
                QtGui.qApp.processEvents()

                if os.path.isfile(str(self.pathTrabalho) + '\\' + arq) == True:
                    self.statusBar().showMessage("Lendo: " + arq)

                    if len(padraoStrCorrente.findall(arq)):
                        data = genfromtxt(str(self.pathTrabalho) + '\\' + arq)
                        I = data[:, 1]

                        # Grafico superior é corrente
                        plt.subplot(211)
                        plt.plot(arange(0, len(I)), I)

                    if len(padraoStrTensao.findall(arq)):
                        data = genfromtxt(str(self.pathTrabalho) + '\\' + arq)
                        V = data[:, 1]

                        # Grafico inferior é tensão
                        plt.subplot(212)
                        plt.plot(arange(0, len(V)), V)

                        pastaComDados += 1

                cont = cont + 1
                self.progressBar.setValue(100 * (cont / len(conteudoPasta)))

            self.progressBar.setEnabled(False)
            print u'aviso: plotGrafico: fim do plot'
            self.statusBar().showMessage(u"Fim do plot")

            if pastaComDados:
                plt.subplot(211)
                plt.xlabel(u'Amostra')
                plt.ylabel(u'Corrente')
                plt.subplot(212)
                plt.xlabel(u'Amostra')
                plt.ylabel(u'Tensão')

                plt.show()
            else:
                self.pathTrabalho = 0
                QtGui.QMessageBox.warning(self, u"Erro", u"Esta pasta não contém nenhum arquivo válido")

        else:
            print u'erro: pasta com os dados das amostras nao selecionada'
            QtGui.QMessageBox.warning(self, "Erro", u"Selecione pasta com os dados das amostras para continuar")
            self.pathTrabalho = QtGui.QFileDialog.getExistingDirectory(self, "Area de Trabalho")
            print self.pathTrabalho
            self.statusBar().showMessage("path de trabalho: %s" % (self.pathTrabalho))
            self.statusBar

            if self.pathTrabalho:
                self.plotGrafico()

    def pos_analise(self):
        print u'aviso: pos_analise: iniciando'

        try:
            arquivo = str(QtGui.QFileDialog.getOpenFileName(self, u'Amostras Anteriores', self.areaTrabalho))
            print arquivo
        except:
            print 'erro: posanalise: erro na leitura do arquivo'
            return

        m = u"Carregando amostras anteriores"

        self.statusBar().showMessage(m)
        self.label_4.setText(m)

        data = loadmat(arquivo)
        V1 = data['V1'].squeeze()
        I1 = data['I1'].squeeze()

        V1 = np.delete(V1,0,1)
        I1 = np.delete(I1,0,1)

        m = u"Iniciando análise"

        self.statusBar().showMessage(m)
        self.label_4.setText(m)

        tipo, num_exato = pat.returnNumberRods(V1, I1)

        if tipo[0] == 0:
            msgHastes = "1 a 2 hastes"
        elif tipo[0] == 1:
            msgHastes = "3 a 4 hastes"
        elif tipo[0] == 'erro':
            msgHastes = 'ERRO'
        else:
            msgHastes = "Nenhuma haste, %s" % (str(tipo))

        self.label_7.setText(msgHastes)
        self.label_31.setText(str(num_exato))

        m = u"Parado"

        self.statusBar().showMessage(m)
        self.label_4.setText(m)

    def salvaAreaTrabalhoTXT(self):
        try:
            arq = open('.conf_areaTrabalho', 'w')
            arq.write(self.areaTrabalho)
            arq.close()
            return 0
        except:
            print u'salvaAreaTrabalhoTXT: erro: nao foi possivel criar arquivo'
            return -1

    def lerAreaTrabalhoTXT(self):
        self.areaTrabalhoTXT = ''
        try:
            arq = open('.conf_areaTrabalho', 'r')
            self.areaTrabalhoTXT = arq.read()
            arq.close()
            return 0
        except:
            print u'lerAreaTrabalhoTXT: erro: não foi póssivel ler arquivo'
            return -1

    def msgBoxERRO(self):
        QtGui.QMessageBox.warning(self, "Erro", u"Pota essa porra no chão, não porra!\nRodrigo Paulino")
        return 0

    def treinar_modelo(self):
        msg = u'Iniciando o treinamento do modelo...'
        print msg
        self.statusBar().showMessage(msg)
        pat.trainAndStoreTheModel()

        msg = u'Fim do treinamento'
        print msg
        self.statusBar().showMessage(msg)

    def cancelar(self):
        if self.fInicioProcesso:
            print u'Cancelando a aquisição...'
            self.statusBar().showMessage(u'Cancelando a aquisição...')
            self.label_4.setText(u'Cancelando...')
            self.fCancelar = 1
        else:
            print u'Só é póssivel cancelar algo que foi iniciado!'
            self.statusBar().showMessage(u'Só é póssivel cancelar algo que foi iniciado!')


    def screen_aumento(self):
        self.padrao_width = 800
        self.padrao_height = 600

        self.showMaximized()

        print u'Dimensões atuais'
        print self.width()
        print self.height()
        print self.depth()

        dif_width = abs(self.padrao_width - self.width())
        dif_height = abs(self.padrao_height - self.height())
        dif_p_width = abs(self.padrao_width - self.width())/self.padrao_width
        dif_p_height = abs(self.padrao_height - self.height())/self.padrao_height

        print 'Diferença:', dif_height, dif_width
        print 'Percentual:', dif_p_height, dif_p_width


if __name__ == "__main__":
    print u'Iniciando a interface grafica para o sistema de aquisicao'
    print u'Projeto: Sistema de Aterramento'

    a = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(a.exec_())
