#!/usr/bin/env python3
"""
Main file for app, a mind mapping tool


author : 'Aurelien Cibrario <aurelien.cibrario@gmail.com>'

"""

import sys
# from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from src.gui.mainwindow import Ui_MainWindow

# First compile the ui files
uic.compileUiDir('src/gui')

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.parent = parent

        # Apply Ui setup
        self.setupUi(self)



class Arbo(QApplication):

    def run(self):
        w = MainWindow()
        w.show()

        return(self.exec_())



