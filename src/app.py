#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main file for app, a mind mapping tool


author : 'Aurelien Cibrario <aurelien.cibrario@gmail.com>'

"""

import sys
import platform
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import src.CompileUiFiles
from src.gui.GenericEventFilter import GenericEventFilter
import src.gui as Argui
from src.data import idea_manager as ArData
import src.data as ArData




class MainWindow(QMainWindow):
    """
    Main Windows. Map entry points.
    """

    def __init__(self, parent=None, qtflags=0):
        QMainWindow.__init__(self)

        # Make sure my laptop find the right theme to display icons
        if QIcon.themeName() == '' and 'LinuxMintseitur' in platform.platform():
            QIcon.setThemeName('Mint-X')

        # Apply Ui setup
        self.ui = Argui.Ui_MainWindow()
        self.ui.setupUi(self)

        # Instantiate IdeaManager
        self.ideamanager = ArData.IdMan()

        # Create dict to open multiple map widgets
        self.map_windows = {}



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
        """
        Dealing with custom connections
        Note that connection to actions are automatically done with the name
        """
        self.ui.table_view.doubleClicked.connect(self.on_table_double_click)

        """
        Dealing with view model
        """
        # Create model for ideas viewing
        self.table_view_model = QStandardItemModel()
        #  Get Idea features labels and assign to model
        labels = [x for x in ArData.Idea.features_dict().values()]
        self.table_view_model.setHorizontalHeaderLabels(labels)

        # Assign model to table
        self.ui.table_view.setModel(self.table_view_model)

        # Load stored ideas
        for idea in self.ideamanager.loadall():
            self.add_idea_to_model(idea, self.table_view_model)



        # Instance Generic event filter and attach
        self.generic_filter = GenericEventFilter(False)#, 10, 11, 12, 110)
        self.installEventFilter(self.generic_filter)

    def add_idea_to_model(self, idea, model):
        """
        Add given idea to given model

        Create a list of QStandardItem and add to given model.
        Add idea's uuid to fist item

        :param model: a QStandartItemModel
        :param idea: an idea to display
        """
        # Get the features names
        feature_names = [x for x in idea.features_dict()]
        # Generate list of QstandartItem
        item_list = [QStandardItem(getattr(idea, x)) for x in feature_names]
        # Put UUID in first item to keep trace
        # First item in line will be returned by QStandardItemModel.selectionModel().selectedRows()
        item_list[0].uuid = idea.uuid

        # Append row to model
        model.appendRow(item_list)

    @pyqtSlot()
    def on_table_double_click(self):
        sender = self.sender()
        index = sender.selectionModel().selectedRows()
        item = self.table_view_model.itemFromIndex(index[0])
        #print(item.uuid)

        self.map_windows[item.uuid] = Argui.MapWindow()
        self.map_windows[item.uuid].setWindowTitle('Map around {}'.format(item.text()))
        self.map_windows[item.uuid].show()

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
            # New idea
            idea = ArData.Idea()
            # add info from dialog
            idea.title = w.ui.title_input.text()
            idea.comment = w.ui.comment_input.text()

            self.add_idea_to_model(idea, self.table_view_model)
            self.ideamanager.save(idea)

    @pyqtSlot()
    def on_action_delete_triggered(self):
        # get mouse selection
        indexes = self.ui.table_view.selectionModel().selectedRows()

        # get uuid in
        # first item and delete idea
        for index in indexes:
            item = self.table_view_model.itemFromIndex(index)
            self.ideamanager.delete(item.uuid)

        # remove all selected rows
        self.table_view_model.removeRows(indexes[0].row(), len(indexes))

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


