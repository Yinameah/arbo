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
        self.label = QtWidgets.QLabel(NewIdeaDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(NewIdeaDialog)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(NewIdeaDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(NewIdeaDialog)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(NewIdeaDialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(NewIdeaDialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
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
        self.label.setText(_translate("NewIdeaDialog", "Input 1 :"))
        self.label_2.setText(_translate("NewIdeaDialog", "foo :"))
        self.label_3.setText(_translate("NewIdeaDialog", "bar :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewIdeaDialog = QtWidgets.QDialog()
    ui = Ui_NewIdeaDialog()
    ui.setupUi(NewIdeaDialog)
    NewIdeaDialog.show()
    sys.exit(app.exec_())

