# -*- coding: utf-8 -*-
from django import forms 
from dynamicforms.utils import get_field_class, get_field_defaults

def build_form(form_instance):
    '''
    Build's form
    Else builds form by data that get's form db
    :return: Builded form
    '''
    form_data = { '__doc__': form_instance.description}

    #generating fields for form
    for field_obj in form_instance.fields.all():
        field_class = get_field_class(field_obj.field)
        defaults = get_field_defaults(field_obj.field)
        field = field_class(label=field_obj.label,
                            help_text=field_obj.help_text,
                            **defaults)
        form_data[field_obj.field_name] = field
    metaclass = forms.Form.__metaclass__

    new_form = metaclass(str(form_instance.name),
                         (forms.Form,),
                         form_data)
    return new_form
