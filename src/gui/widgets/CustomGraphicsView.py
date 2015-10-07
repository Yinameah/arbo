from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from src.gui.GenericEventFilter import GenericEventFilter


class CustomGraphicsView(QGraphicsView):

    def __init__(self, parent):
        QGraphicsView.__init__(self, parent)

        self._view_scale = 1

        self.setDragMode(QGraphicsView.RubberBandDrag)



    def mouseMoveEvent(self, event):
        #print('move event intercepted by render area @ {}'.format(event.pos()))
        # Warning : QGraphicsItem receive event after QGraphicsView
        super().mouseMoveEvent(event)

    def keyPressEvent(self, event):
        # Use space to move view only if mouse is on it
        if event.key() == Qt.Key_Space and not event.isAutoRepeat():
            # Hand cursor to drag
            self.setCursor(Qt.OpenHandCursor)
            # Drag policy
            self.setDragMode(QGraphicsView.ScrollHandDrag)
            self.setInteractive(False)
        else:
            super().keyPressEvent(event)

    def keyReleaseEvent(self, event):
        # Use space to move view only if mouse is on it
        if event.key() == Qt.Key_Space and not event.isAutoRepeat():
            # Cursor back to normal
            self.setCursor(Qt.ArrowCursor)
            # Back to selection policy
            self.setDragMode(QGraphicsView.RubberBandDrag)
            self.setInteractive(True)
        else:
            super().keyPressEvent(event)

    def wheelEvent(self, event):
        self._view_scale = 1 + event.angleDelta().y()/1200
        self.scale(self._view_scale, self._view_scale)

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)


