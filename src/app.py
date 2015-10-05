#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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

import src.gui as Argui
from src.data import idea_manager as ArData
import src.data as ArData


class GenericEventFilter(QObject):
    """
    Affiche tous les types d'event sur stout pour aider à la création
    On peut l'instancier avec un type (QEvent class) pour ne trier que ceux-là
    """

    def __init__(self, display, *args):
        QObject.__init__(self)

        if args == ():
            args = 'all'
        self.event_type_to_filter = args
        self.display = display

    def eventFilter(self, receiver, event):
        # print all
        if self.display and self.event_type_to_filter == 'all':
            print("{} received event {} with QEvent number {}".format(
                receiver.objectName(), type(event), event.type()))
            return False
        # print all event in args
        elif self.display and event.type() in self.event_type_to_filter:
            print("{} received event {} with QEvent number {}".format(
                receiver.objectName(), type(event), event.type()))
            return False
        # display false without args : nothing to print
        elif not self.display and self.event_type_to_filter == 'all':
            return False
        # display false : print other than in args
        elif not self.display and event.type() not in self.event_type_to_filter:
            print("{} received event {} with QEvent number {}".format(
                receiver.objectName(), type(event), event.type()))
            return False
        # all other events
        else:
            return super().eventFilter(receiver, event)


class MainWindow(QMainWindow):
    """
    Main Windows. Map entry points.
    """

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.parent = parent

        # Make sure my laptop find the right theme to display icons
        if QIcon.themeName() == '' and 'LinuxMintseitur' in platform.platform():
            QIcon.setThemeName('Mint-X')

        # Apply Ui setup
        self.ui = Argui.Ui_MainWindow()
        self.ui.setupUi(self)

        # Instantiate IdeaManager
        self.ideamanager = ArData.IdMan()

        # Instance Generic event filter and attach
        self.generic_filter = GenericEventFilter(False)#, 10, 11, 12, 110)
        self.ui.table_view.installEventFilter(self.generic_filter)


        # b1 = QPushButton('test', self.ui_central_widget)
        # b1.setObjectName('Bouton Hello')
        # self.horizontalLayout.addWidget(b1)
        data = ['test','bla','truc','bidule']

        #self.items = []
        #for i in range(4):
        #    self.items.append(QStandardItem('test {}'.format(i)))
        #self.items2 = []
        #for i in range(4, 7):
        #    self.items2.append(QStandardItem('test {}'.format(i)))

        #self.model.setRowCount(5)
        #self.model.setHorizontalHeaderLabels(data)

        #self.model.insertRow(1, self.items)
        #self.model.insertRow(5, self.items2)

        self.table_view_model = QStandardItemModel()
        self.ui.table_view.setModel(self.table_view_model)

        # Load stored ideas
        self.table_view_model.appendRow()




    @pyqtSlot()
    def on_action_new_triggered(self):
        #self.add_count += 1
        #count = self.table_view_model.rowCount()
        #print(count)
        #self.table_view_model.insertRow(count, [QStandardItem('test {}'.format(self.add_count)), QStandardItem('machin')])

        # Create dialog
        w = QDialog(self)
        w.ui = Argui.Ui_NewIdeaDialog()
        w.ui.setupUi(w)
        # When dialog is accepted, create idea, store and display
        ok = w.exec()
        if ok:
            idea = ArData.Idea()
            idea.title = w.ui.title_input.text()
            idea.comment = w.ui.comment_input.text()
        self.ideamanager.save(idea)
        self.table_view_model.appendRow([QStandardItem(idea.title), QStandardItem(idea.comment)])



    @pyqtSlot()
    def on_action_delete_triggered(self):
        indexes = self.ui.table_view.selectionModel().selectedRows()
        for index in indexes:
            self.table_view_model.removeRow(index.row())

    @pyqtSlot()
    def on_action_about_triggered(self):
        w = QDialog(self)
        constructor = Argui.Ui_DialogAbout()
        constructor.setupUi(w)
        w.show()

    @pyqtSlot()
    def on_action_edit_triggered(self):
        row = self.ui.table_view.currentIndex()
        print(row.row())



class Arbo(QApplication):

    def __init__(self, args):
        super().__init__(args)

    def run(self):
        w = MainWindow()
        w.show()

        return(self.exec())


