#!/usr/bin/env python3
"""
Main file for app, a mind mapping tool


author : 'Aurelien Cibrario <aurelien.cibrario@gmail.com>'

"""

import sys
# from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.parent = parent

        uic.loadUi('src/GUI/testmain.ui', self)

        self.resize(100, 100)



class Arbo(QApplication):

    def run(self):
        w = MainWindow()
        w.show()

        return(self.exec_())



