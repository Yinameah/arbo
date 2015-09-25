# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/gui/MainWindow.ui'
#
# Created: Fri Sep 25 15:22:20 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 600)
        icon = QtGui.QIcon.fromTheme("applications-utilities")
        MainWindow.setWindowIcon(icon)
        MainWindow.setAccessibleName("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listView2 = QtWidgets.QListView(self.centralwidget)
        self.listView2.setObjectName("listView2")
        self.horizontalLayout.addWidget(self.listView2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.mainMenuBar = QtWidgets.QMenuBar(MainWindow)
        self.mainMenuBar.setGeometry(QtCore.QRect(0, 0, 801, 25))
        self.mainMenuBar.setObjectName("mainMenuBar")
        self.menuHelp = QtWidgets.QMenu(self.mainMenuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFile = QtWidgets.QMenu(self.mainMenuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.mainMenuBar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setCheckable(False)
        self.actionNew.setChecked(False)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("document-open")
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("edit-delete")
        self.actionDelete.setIcon(icon)
        self.actionDelete.setObjectName("actionDelete")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("application-exit")
        self.actionQuit.setIcon(icon)
        self.actionQuit.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionQuit.setObjectName("actionQuit")
        self.mainToolBar.addAction(self.actionNew)
        self.mainToolBar.addAction(self.actionOpen)
        self.mainToolBar.addAction(self.actionDelete)
        self.menuHelp.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionDelete)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.mainMenuBar.addAction(self.menuFile.menuAction())
        self.mainMenuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)
        self.actionAbout.triggered.connect(MainWindow.on_actionAboutTriggered)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Arbo"))
        self.mainToolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menuHelp.setTitle(_translate("MainWindow", "?"))
        self.menuFile.setTitle(_translate("MainWindow", "Fichier"))
        self.actionAbout.setText(_translate("MainWindow", "À propos"))
        self.actionNew.setText(_translate("MainWindow", "Nouveau"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Ouvrir"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionDelete.setText(_translate("MainWindow", "Effacer"))
        self.actionQuit.setText(_translate("MainWindow", "Quitter"))
        self.actionQuit.setIconText(_translate("MainWindow", "Quitter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

