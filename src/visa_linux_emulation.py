# -*- coding: utf-8 -*-
# Apenas o básico, para pequenas alterações no linux
# esse codigo é apenas temporário, não sendo necessário
# quando visa estiver funcionando corretamento no linux
#
# UFC - Universidade de Federal do Ceará
#
# Responsáveis:
# Felipe Bandeira da Silva
# Francisco Alexander
#

__author__ = 'felipe'

def get_instruments_list():
    return ['Agilent Emulador', '']

class instrument():
    def __init__(self):
        pass
    def ask(self, entrada):
        if entrada == '*IDN?':
            return 'Agilent U2531A emulado'

