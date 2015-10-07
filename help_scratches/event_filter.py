"""
Working event Filter exemple. Here to remember
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MyEventFilter(QObject):

    # Override eventFilter pour faire des trucs
    # Tous les events auquel est attaché le filtre vont passer là
    def eventFilter(self, receiver, event):
        # N'agit que sur les event de type "ButtonPress"
        if event.type() == QEvent.MouseButtonPress:
            # Do Stuff
            print('click with button {} @ {}, {}'.format(event.button(), event.x(), event.y()))
            # Avec False, l'event n'est pas considéré comme traité. Il va être géré plus loin
            # Mettre True si le bouton ne doit pas agir ailleurs (par exemple via un slot)
            return False
        # S'il s'agit d'un autre type d'event
        else:
            # On appelle la fonction de la classe parente pour continuer le boulot
            return super().eventFilter(receiver, event)


class MyWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.resize(300, 300)

        self.but = QPushButton(self)
        self.but.setText('hello')
        self.but2 = QPushButton(self)
        self.but2.setText('truc')
        self.but2.move(30, 30)

        # On instancie un filtre, et on l'attache à un objet
        self.myfilter = MyEventFilter()
        self.but2.installEventFilter(self.myfilter)


        self.show()


        self.but.clicked.connect(self.on_but_clicked)
        self.but2.clicked.connect(self.on_but_clicked)


    def on_but_clicked(self):
        sender = self.sender()
        print("clické sur le bouton '{}'!!!".format(sender.text()))


def main():
    app = QApplication(sys.argv)
    w = MyWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
