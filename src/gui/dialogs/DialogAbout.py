# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/gui/dialogs/DialogAbout.ui'
#
# Created: Fri Sep 25 15:22:20 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogAbout(object):
    def setupUi(self, DialogAbout):
        DialogAbout.setObjectName("DialogAbout")
        DialogAbout.resize(401, 314)
        icon = QtGui.QIcon.fromTheme("help-about")
        DialogAbout.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogAbout)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelAbout = QtWidgets.QLabel(DialogAbout)
        self.labelAbout.setWordWrap(True)
        self.labelAbout.setObjectName("labelAbout")
        self.verticalLayout.addWidget(self.labelAbout)
        self.closeAbout = QtWidgets.QPushButton(DialogAbout)
        self.closeAbout.setObjectName("closeAbout")
        self.verticalLayout.addWidget(self.closeAbout)
        self.labelAbout.setBuddy(self.labelAbout)

        self.retranslateUi(DialogAbout)
        self.closeAbout.clicked.connect(DialogAbout.close)
        QtCore.QMetaObject.connectSlotsByName(DialogAbout)

    def retranslateUi(self, DialogAbout):
        _translate = QtCore.QCoreApplication.translate
        DialogAbout.setWindowTitle(_translate("DialogAbout", "Arbo - About"))
        self.labelAbout.setText(_translate("DialogAbout", "<html><head/><body><p><img src=\":/icons/main.svg\"/><span style=\" font-size:12pt; font-weight:600; vertical-align:middle;\">Arbo 0.01</span></p><p>Arbo is a simple and original mind mapping tool.</p><p><br/>Instead of having one or multiple start point like moste similar tools, it works with Labels and has no particular organisation which let you make your own.</p><p><br/></p><p>Liscence : blabla</p></body></html>"))
        self.closeAbout.setText(_translate("DialogAbout", "Fermer"))

from . import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogAbout = QtWidgets.QDialog()
    ui = Ui_DialogAbout()
    ui.setupUi(DialogAbout)
    DialogAbout.show()
    sys.exit(app.exec_())

