from PyQt5.QtCore import *

class GenericEventFilter(QObject):
    """
    Affiche tous les types d'event sur stout pour aider au développement
    On peut l'instancier avec un type (QEvent class) pour ne trier que ceux-là
    """

    def __init__(self, display, *args):
        QObject.__init__(self)

        if args == ():
            args = 'all'
        self.event_type_to_filter = args
        self.display = display

    def eventFilter(self, receiver, event):
        # print all
        if self.display and self.event_type_to_filter == 'all':
            print("{} received event {} with QEvent number {}".format(
                receiver.objectName(), type(event), event.type()))
            return False
        # print all event in args
        elif self.display and event.type() in self.event_type_to_filter:
            print("{} received event {} with QEvent number {}".format(
                receiver.objectName(), type(event), event.type()))
            return False
        # display false without args : nothing to print
        elif not self.display and self.event_type_to_filter == 'all':
            return False
        # display false : print other than in args
        elif not self.display and event.type() not in self.event_type_to_filter:
            print("{} received event {} with QEvent number {}".format(
                receiver.objectName(), type(event), event.type()))
            return False
        # all other events
        else:
            return super().eventFilter(receiver, event)
