# -*- coding: utf-8 -*-
import sys

from django.utils.translation import ugettext_lazy as _

from dynamicforms.exceptions import FieldDidNotRegister


def build_available_field_list():
    '''
    Returns list of tuple for field choices
    Tuple:
    (field_path, field_name, default)
    :param field_path: path to field
    :type field_path: unicode string
    :param field_name: name that will be displayed on selecting field
    :type field_name: unicode string
    :param default: default values for current field
    :type default: dict
    '''
    return [('django.forms.CharField', _('Char field'), {'max_length': 50}),
            ('django.forms.IntegerField', _('Integer field'), {}),
            ('django.forms.BooleanField', _('Boolean field'), {})]

def get_choices_field_list():
    '''
    Returns list of available fields for choices in :class:`dynamicforms.models.Field`
    '''
    return [(path, name)
            for path, name, defaults in build_available_field_list()]

def get_field_class(field_path):
    '''
    Imports field class from field_path and returns class
    '''
    module_path = '.'.join(field_path.split('.')[:-1])
    field_class_name = field_path.split('.')[-1]

    __import__(module_path)
    module = sys.modules[module_path]
    return getattr(module, field_class_name, None)

def get_field_defaults(field_path):
    '''
    Returns defaults by field_path
    else raise exception no field with this path
    '''
    field_list = build_available_field_list()
    info = dict(((path, defaults) for path, name, defaults in field_list))
    try:
        return info[field_path]
    except KeyError:
        raise FieldDidNotRegister(field_path)
