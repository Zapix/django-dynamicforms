# -*- coding: utf-8 -*-
from django import forms as djforms

from dynamicforms import models
from dynamicforms.utils import get_field_class, get_field_defaults
from dynamicforms.exceptions import FormDoesNotExist

class FormsLazyObject(object):

    def __init__(self):
        self._forms = {}

    def __getattr__(self, name):
        '''
        Returns form class:
        Checks have we build asking form class.
        If we build return this class.
        Checks have we got info about this class
        on db.
        If yes we build form class and return in.
        Else raise excpetion that form DoesNotExist
        '''
        if name in self._forms:
            return self._forms[name]

        try:
            form_instance = models.DynamicForm.objects.get(name=name)
            form_data = { '__doc__': form_instance.description}

            #generating fields for form
            for field_obj in form_instance.fields.all():
                field_class = get_field_class(field_obj.field)
                defaults = get_field_defaults(field_obj.field)
                form_data[field_obj.field_name] = field_class(
                                                       label=field_obj.label,
                                                       required=True,
                                                       **defaults
                                                       )
            
            metaclass = djforms.Form.__metaclass__

            self._forms[form_instance.name] = metaclass(
                                                   str(form_instance.name),
                                                   (djforms.Form,),
                                                   form_data)
            return self._forms[form_instance.name]

        except models.DynamicForm.DoesNotExist:
            raise FormDoesNotExist(name)
        
        def __setattr__(self, name, value):
            pass
        
        def __delattr__(self, name):
            pass

forms = FormsLazyObject()

