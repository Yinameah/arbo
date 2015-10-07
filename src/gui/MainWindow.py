# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/aurelien/sketchbook/arbo/src/gui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 599)
        icon = QtGui.QIcon.fromTheme("applications-utilities")
        MainWindow.setWindowIcon(icon)
        MainWindow.setAccessibleName("")
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.table_view = QtWidgets.QTreeView(self.central_widget)
        self.table_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.table_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_view.setObjectName("table_view")
        self.horizontalLayout.addWidget(self.table_view)
        MainWindow.setCentralWidget(self.central_widget)
        self.main_tool_bar = QtWidgets.QToolBar(MainWindow)
        self.main_tool_bar.setObjectName("main_tool_bar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.main_tool_bar)
        self.main_menu_bar = QtWidgets.QMenuBar(MainWindow)
        self.main_menu_bar.setGeometry(QtCore.QRect(0, 0, 801, 25))
        self.main_menu_bar.setObjectName("main_menu_bar")
        self.menu_help = QtWidgets.QMenu(self.main_menu_bar)
        self.menu_help.setObjectName("menu_help")
        self.menu_file = QtWidgets.QMenu(self.main_menu_bar)
        self.menu_file.setObjectName("menu_file")
        MainWindow.setMenuBar(self.main_menu_bar)
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_new = QtWidgets.QAction(MainWindow)
        self.action_new.setCheckable(False)
        self.action_new.setChecked(False)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.action_new.setIcon(icon)
        self.action_new.setObjectName("action_new")
        self.action_delete = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("edit-delete")
        self.action_delete.setIcon(icon)
        self.action_delete.setObjectName("action_delete")
        self.action_quit = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("application-exit")
        self.action_quit.setIcon(icon)
        self.action_quit.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_quit.setObjectName("action_quit")
        self.action_cursor = QtWidgets.QAction(MainWindow)
        self.action_cursor.setObjectName("action_cursor")
        self.action_edit = QtWidgets.QAction(MainWindow)
        self.action_edit.setObjectName("action_edit")
        self.main_tool_bar.addAction(self.action_new)
        self.main_tool_bar.addAction(self.action_delete)
        self.menu_help.addAction(self.action_about)
        self.menu_file.addAction(self.action_new)
        self.menu_file.addAction(self.action_edit)
        self.menu_file.addAction(self.action_delete)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_quit)
        self.main_menu_bar.addAction(self.menu_file.menuAction())
        self.main_menu_bar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Arbo"))
        self.main_tool_bar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menu_help.setTitle(_translate("MainWindow", "?"))
        self.menu_file.setTitle(_translate("MainWindow", "Fichier"))
        self.action_about.setText(_translate("MainWindow", "À propos"))
        self.action_new.setText(_translate("MainWindow", "Nouveau"))
        self.action_new.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_delete.setText(_translate("MainWindow", "Effacer"))
        self.action_delete.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.action_quit.setText(_translate("MainWindow", "Quitter"))
        self.action_quit.setIconText(_translate("MainWindow", "Quitter"))
        self.action_cursor.setText(_translate("MainWindow", "changer curseur"))
        self.action_edit.setText(_translate("MainWindow", "Editer"))
        self.action_edit.setShortcut(_translate("MainWindow", "Ctrl+E"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

