#!/usr/bin/env python3
"""
Main file for app, a mind mapping tool


author : 'Aurelien Cibrario <aurelien.cibrario@gmail.com>'

"""

# First compile the ui/rc files / debugging state
from PyQt5 import uic
uic.compileUiDir('src/gui', recurse=True, from_imports=True, execute=True, resource_suffix='')
from subprocess import call
call(['pyrcc5', 'src/gui/icons/icons_rc.qrc', '-o', 'src/gui/icons/icons_rc.py'])

import sys
import platform
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import src.gui as ArGui


class MainWindow(QMainWindow, ArGui.Ui_MainWindow):
    """
    Main Windows. Map entry points.
    """

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.parent = parent

        # Make sure my laptop find the right theme to display icons
        if QIcon.themeName() == '' and platform.system()=='Linux':
            QIcon.setThemeName('Mint-X')


        # Apply Ui setup
        self.setupUi(self)


        #b = QPushButton(self)
        #icon = QIcon(':/main.svg')
        #print(icon)
        #b.setIcon(icon)
        self.on_actionAboutTriggered()



    def on_actionAboutTriggered(self):

        w = QDialog(self)
        constructor = ArGui.Ui_DialogAbout()
        constructor.setupUi(w)
        w.show()


    def closeEvent(self, event):
        pass






class Arbo(QApplication):

    def __initi__(self, args):
        print(args)
        QApplication.__init__('')

        print('app launch')
        print(QApplication.desktopSettingsAware())

    def run(self):
        w = MainWindow()
        w.show()

        return(self.exec_())


