# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/aurelien/sketchbook/arbo/src/gui/widgets/MapWidget.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MapWidget(object):
    def setupUi(self, MapWidget):
        MapWidget.setObjectName("MapWidget")
        MapWidget.resize(760, 511)
        self.horizontalLayout = QtWidgets.QHBoxLayout(MapWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.graphics_view = CustomGraphicsView(MapWidget)
        self.graphics_view.setObjectName("graphics_view")
        self.horizontalLayout.addWidget(self.graphics_view)

        self.retranslateUi(MapWidget)
        QtCore.QMetaObject.connectSlotsByName(MapWidget)

    def retranslateUi(self, MapWidget):
        _translate = QtCore.QCoreApplication.translate
        MapWidget.setWindowTitle(_translate("MapWidget", "Map"))

from src.gui.widgets.CustomGraphicsView import CustomGraphicsView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MapWidget = QtWidgets.QWidget()
    ui = Ui_MapWidget()
    ui.setupUi(MapWidget)
    MapWidget.show()
    sys.exit(app.exec_())

