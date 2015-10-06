#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
import os
from PyQt5.QtGui import QStandardItemModel


from src.data.ideas import Idea


IDEAS_MANIFEST_LOCATION = os.path.expanduser('~/.arbo/ideas/manifest.idea')
IDEAS_STORE_LOCATION = os.path.expanduser('~/.arbo/ideas/')

class IdMan(object):
    _is_instance = False
    _instance = None

    # Remimplement new to have only one instance of IdMan
    def __new__(cls, *args, **kwargs):
        if cls._is_instance :
            return cls._instance
        else:
            cls._is_instance = True
            obj = super().__new__(cls)
            cls._instance = obj
            return obj

    def __init__(self):
        with open(IDEAS_MANIFEST_LOCATION, 'r') as f:
            self.manifest = yaml.safe_load(f)
            #print('manifest : {}'.format(self.manifest))

    def save(self, idea):
        # Path manipulation to store ideas
        # TODO : autre méthode "create" ou bien test de l'existance du fichier dans la méthode save ?
        filename = str(idea.uuid)+'.idea'
        file = os.path.join(IDEAS_STORE_LOCATION, filename)

        # YAML dump and write to file
        output = yaml.safe_dump(idea.__dict__)
        with open(file, 'a') as f:
            print(output, file=f)

        self.manifest.append(idea.uuid)
        with open(IDEAS_MANIFEST_LOCATION, 'w') as f:
            yaml.safe_dump(self.manifest, f)

    def loadall(self):
        for idea in self.manifest:
            yield self.load(idea)


    def load(self, uuid_to_load):
        # Path manipulation to get ideas
        filename = str(uuid_to_load)+'.idea'
        file = os.path.join(IDEAS_STORE_LOCATION, filename)
        # New idea, load data in it
        try:
            with open(file, 'r') as f:
                y_result = yaml.load(f)
                #print(y_result)
        except (IOError, OSError):
            print('putain, ça a merdé !!')
            print("une idée n'a pas été retrouvée, on va l'enlever du manifeste")
            self.manifest.remove(uuid_to_load)
            self.save_manifest()
            return None
        else:
            idea = Idea()
            idea.__dict__ = y_result
            return idea

    def delete(self, uuid_to_delete):
        filename = str(uuid_to_delete)+'.idea'
        file = os.path.join(IDEAS_STORE_LOCATION, filename)
        # delete files
        os.remove(file)
        # remove from manifest
        self.manifest.remove(uuid_to_delete)
        self.save_manifest()

    def save_manifest(self):
        with open(IDEAS_MANIFEST_LOCATION, 'w') as f:
            yaml.safe_dump(self.manifest, f)



if __name__ == '__main__':

    ideamanager = IdMan()

    #one_idea = Idea()
    #one_idea.title = 'Test'
    #one_idea.comment = 'Un commentaire pour tester'

    #ideamanager.save(one_idea)

    for idea in ideamanager.loadall():
        print(idea)


    #ret_idea = ideamanager.load('493fadca-ca91-47a6-9e45-ed72eac99824')
    #print(ret_idea)




