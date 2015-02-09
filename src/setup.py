from distutils.core import setup
import py2exe
import numpy

setup(
    version = "1.0.0",
    description = "Sistema de Aterramento",
    name = "labterra",
    windows = ["acoes_interface.pyw"],
    )
