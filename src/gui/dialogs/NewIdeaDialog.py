# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/gui/dialogs/NewIdeaDialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewIdeaDialog(object):
    def setupUi(self, NewIdeaDialog):
        NewIdeaDialog.setObjectName("NewIdeaDialog")
        NewIdeaDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        NewIdeaDialog.resize(639, 459)
        NewIdeaDialog.setFocusPolicy(QtCore.Qt.NoFocus)
        self.verticalLayout = QtWidgets.QVBoxLayout(NewIdeaDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.title_label = QtWidgets.QLabel(NewIdeaDialog)
        self.title_label.setObjectName("title_label")
        self.horizontalLayout.addWidget(self.title_label)
        self.title_input = QtWidgets.QLineEdit(NewIdeaDialog)
        self.title_input.setObjectName("title_input")
        self.horizontalLayout.addWidget(self.title_input)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comment_label = QtWidgets.QLabel(NewIdeaDialog)
        self.comment_label.setObjectName("comment_label")
        self.horizontalLayout_2.addWidget(self.comment_label)
        self.comment_input = QtWidgets.QLineEdit(NewIdeaDialog)
        self.comment_input.setObjectName("comment_input")
        self.horizontalLayout_2.addWidget(self.comment_input)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewIdeaDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(NewIdeaDialog)
        self.buttonBox.accepted.connect(NewIdeaDialog.accept)
        self.buttonBox.rejected.connect(NewIdeaDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewIdeaDialog)

    def retranslateUi(self, NewIdeaDialog):
        _translate = QtCore.QCoreApplication.translate
        NewIdeaDialog.setWindowTitle(_translate("NewIdeaDialog", "Nouvelle Idée"))
        self.title_label.setText(_translate("NewIdeaDialog", "Titre :"))
        self.comment_label.setText(_translate("NewIdeaDialog", "Autre champ :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewIdeaDialog = QtWidgets.QDialog()
    ui = Ui_NewIdeaDialog()
    ui.setupUi(NewIdeaDialog)
    NewIdeaDialog.show()
    sys.exit(app.exec_())

