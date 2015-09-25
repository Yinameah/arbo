#!/usr/bin/env python3
"""
Main file for app, a mind mapping tool

Simply import Arbo (application) class and run Qt main loop

author : Aurelien Cibrario <aurelien.cibrario@gmail.com>

"""

import sys
from src.app import Arbo

if __name__ == '__main__':
    #TODO : Vérifier ce qui se passe sur mon autre ordi, est-ce que l'argument gtk est passé automatiquement ?
    arg = ['/home/aurelien/sketchbook/arbo/main.py','-style','gtk']
    app = Arbo(arg)
    sys.exit(app.run())

