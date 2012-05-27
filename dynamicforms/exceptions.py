# -*- coding: utf-8 -*-


class FormDoesNotExist(Exception):
    '''
    Raise when form haven't been founded in db
    '''

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'Form %s does not exist' % self.value


class FieldDidNotRegister(Exception):
    '''
    Raise when info about field haven't been founded
    in build_available_field_list
    '''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'Field(%s) haven\'t been registered' % self.value
