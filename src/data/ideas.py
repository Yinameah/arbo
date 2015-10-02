#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from uuid import uuid4
from math import ceil
import time

class Idea():
    """
    Base class for an idea. Every note/node on the mind map is represented by an idea object
    """

    def __init__(self, title='Empty idea'):
        self.uuid = uuid4()
        self.title = title
        self.link_to = []
        # provisoire
        self.comment = ''

    def link_to(self, uuid):
        self.link_to.append(uuid)

    def unlink_to(self, uuid):
        self.link_to.remove(uuid)


    def unlink_to(self, uuid):
        self.link_to.remove(uuid)


