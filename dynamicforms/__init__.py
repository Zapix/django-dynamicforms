# -*- coding: utf-8 -*-
from django import forms as djforms

from dynamicforms.utils import get_field_class, get_field_defaults
from dynamicforms.exceptions import FormDoesNotExist

class FormsLazyObject(object):

    _forms = {}
    
    def _get_form_info(self, form_name):
        '''
        Tries to find info about form on db.
        If info haven't been found raises :exception:`exceptions.FormDoesNotExist`
        :param form_name: name of form in DB
        :type form_name: string
        :return: object with info about form
        :rtype: :class:`dynamicforms.models.DynamicForm`
        '''
        try:
            #Poor hack for broke import loop
            from dynamicforms.models import DynamicForm
            return  DynamicForm.objects.get(name=form_name)
        except DynamicForm.DoesNotExist:
            raise FormDoesNotExist(form_name)


    def _build_form(self, form_instance):
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
                                required=True,
                                **defaults)
            form_data[field_obj.field_name] = field
        metaclass = djforms.Form.__metaclass__

        new_form = metaclass(str(form_instance.name),
                             (djforms.Form,),
                             form_data)
        return new_form


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
        try:
            return super(FormsLazyObject,
                         self).__getattr__(name)
        except AttributeError:
            pass

        if not name in self._forms:
            form_instance = self._get_form_info(name)
            self._forms[name] = self._build_form(form_instance)
        return self._forms[name]


    def __setattr__(self, name, value):
        pass

    def __delattr__(self, name):
        pass

    def _clear(self, form_name):
        '''
        #Updates exist and have accessed form
        #:param form_instance: instance with form info
        #:type form_instance: :class:`dynamicforms.models.DynamicForm`
        Clears self._forms
        :param form_name: name for delete form
        :type form_name: string
        '''
        if form_name in self._forms:
            del self._forms[form_name]

forms = FormsLazyObject()

