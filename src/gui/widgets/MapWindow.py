#!/usr/bin/env python3

import sys
import src.CompileUiFiles
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from src.gui.GenericEventFilter import GenericEventFilter
from src.gui.widgets.MapWidget import Ui_MapWidget



class MovableRect(QGraphicsRectItem):

    def __init__(self, rectF=None):
        # provide default rectF, @ (0,0) position
        if rectF is None:
            rect = QRectF(0, 0, 100, 100)
        else:
            rect = rectF
        QGraphicsRectItem.__init__(self, rect)

        self._x = 0
        self._y = 0

        # Default visual appearance
        pen = QPen(Qt.DotLine)
        pen.setWidthF(2)
        self.setPen(pen)

        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)


    def contextMenuEvent(self, event):
        print('menu contextuel')

    def mousePressEvent(self, event):
        rect = self.rect()
        #print(rect.size())

    def itemChange(self, change, variant):
        # Check selection change to put the rectangle in red
        if change == QGraphicsItem.ItemSelectedChange:
            if variant:
                pen = self.pen()
                pen.setColor(QColor('red'))
                self.setPen(pen)
            else:
                pen = self.pen()
                pen.setColor(QColor('black'))
                self.setPen(pen)
        else:
            pass
        return super().itemChange(change, variant)




    def isSelected(self):
        print('yahoo')
    # def mousePressEvent(self, event):
    #     print('click @ {} in scene'.format(event.scenePos()))
    #     print('last click @ {} in scene'.format(event.lastScenePos()))
    #     print('')
    #     rect = self.rect()
    #     #rect.translate(event.scenePos())
    #     print(rect.center().translate(event.scenePos()))
    #     self.setRect(rect)
    #
    # def mouseReleaseEvent(self, event):
    #     print('released')
    #
    # def mouseMoveEvent(self, event):
    #     pass




    """
    def mousePressEvent(self, event):

        pen = self.pen()
        pen.setColor(QColor('red'))
        self.setPen(pen)

        self._rect.moveTo(event.pos())
        self.setRect(self._rect)
        print(self._rect.getCoords())
        #print(event.pos())
    """


    """
    Right way to intercept event : def someEvent(self, event):
    Call super().someEvent to let event be intercepted further
    Otherwise, only self will process the event

    Exemple :

    if event.button() == 1:
        print('left button press intercepted on rect')
    elif event.button() == 2:
        print('right button press intercepted on rect')

    super().mousePressEvent(event)
    """

class MapWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        # Apply setupUI
        self.ui = Ui_MapWidget()
        self.ui.setupUi(self)

        scene = QGraphicsScene()
        self.ui.graphics_view.setScene(scene)

        self.rects = []
        self.rects.append(MovableRect())
        self.rects.append(MovableRect())

        for rect in self.rects:
            scene.addItem(rect)




#    def paintEvent(self, event):
#        qp = QPainter()
#        qp.begin(self)
#        self.draw_rect(qp)
#        print(qp)
#        qp.end()
#
#    def draw_rect(self, painter):
#        col = QColor(1, 0, 0)
#        painter.setPen(col)
#
#        painter.drawRect(10, 15, 90, 60)




if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = MapWindow()
    w.show()

    app.exec()

