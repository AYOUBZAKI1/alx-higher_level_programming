#!/usr/bin/python3
'''Module for Base class.'''

class base:
    '''A representation pf the base of our OOP hierarchy.'''

    __nb_objects = 0
    
    def __init__(self, id=None):
        '''constructor.'''
        if id is not None:
            self.id = id
        else:
            base.__nb_objects += 1
            self.id = Base.__nb_objects
