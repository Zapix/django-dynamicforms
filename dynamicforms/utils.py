# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

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
    return [(path, name) for path, name, default in get_choices_field_list()]

