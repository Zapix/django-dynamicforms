# -*- coding: utf-8 -*-
from django import forms as djforms

from dynamicforms import models
from dynamicforms.utils import get_field_class, get_field_defaults
from dynamicforms.exceptions import FormDoesNotExist

class FormsLazyObject(object):

    def __init__(self):
        self._forms = {}

    def _build_form(self, form_name):
        '''
        Build's form
        Tries to find info about form on db.
        If info haven't been found raises :exception:`exceptions.FormDoesNotExist`
        Else builds form by data that get's form db
        :return: Builded form
        '''
        try:
            form_instance = models.DynamicForm.objects.get(name=form_name)
            form_data = { '__doc__': form_instance.description}

            #generating fields for form
            for field_obj in form_instance.fields.all():
                field_class = get_field_class(field_obj.field)
                defaults = get_field_defaults(field_obj.field)
                field = field_class(label=field_obj.label,
                                    help_text=field_obj.help_text,
                                    required=True,
                                    **defaults)
                form_data[field_obj.field_name] = field
            metaclass = djforms.Form.__metaclass__

            new_form = metaclass(str(form_instance.name),
                                 (djforms.Form,),
                                 form_data)
            return new_form

        except models.DynamicForm.DoesNotExist:
            raise FormDoesNotExist(form_name)

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
        if not name in self._forms:
            self._forms[name] = self._build_form(name)
        return self._forms[name]


    def __setattr__(self, name, value):
        pass

    def __delattr__(self, name):
        pass

    def _update(self, form_name):
        '''
        Updates exist and have accessed form
        '''
        if form_name in self._forms:
            self._forms[form_name] = self._build_form(form_name)

forms = FormsLazyObject()

