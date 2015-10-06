#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from uuid import uuid4
from collections import OrderedDict
from math import ceil
import time

class Idea():
    """
    Base class for an idea. Every note/node on the mind map is represented by an idea object
    """

    def __init__(self, title='Empty idea'):
        self.uuid = str(uuid4())
        self.title = title
        self.link_to = []
        # provisoire
        self.comment = ''

    def __repr__(self):
        message = 'This is an {} object stored @ {}\n' \
                  '     Title : {}\n' \
                  '     uuid : {}'.format(self.__class__, id(self), self.title, self.uuid)
        return message

    @staticmethod
    def features_dict(layout='simple'):
        """
        For displaying purposes. Return ordered list of idea's features

        Different layouts could be implemented. 'Simple' is default.
        Use layout = 'complete' to have all features of an idea
        :param layout: simple, complete
        :return: dict of idea's features:name
        """
        features_dict = OrderedDict()
        if layout == 'simple':
            features_dict['title'] = 'Titre'
            features_dict['comment'] = 'Commentaire'
        elif layout == 'complete':
            features_dict['title'] = 'Titre'
            features_dict['comment'] = 'Commentaire'
            features_dict['link_to'] = 'Liens vers'
            features_dict['uuid'] = 'UUID'
        else:
            raise ValueError("You try to use '{}' layout. No such layout.".format(layout))

        return features_dict

    def link_to(self, uuid):
        self.link_to.append(uuid)

    def unlink_to(self, uuid):
        self.link_to.remove(uuid)


if __name__ == '__main__':

    one_idea = Idea()

    for feature, feature_name in one_idea.features_dict().items():
        print(feature, feature_name)

    for feature in Idea.features_dict():
        print(feature)

    for name in Idea.features_dict().values():
        print(name)

    for i, feature in enumerate(Idea.features_dict()):
        print(i, feature)
