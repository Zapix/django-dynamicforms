# -*- coding: utf-8 -*-
from dynamicforms.factory import build_form
from dynamicforms.helpers import get_form_info


class FormsLazyObject(object):

    _forms = {}

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
            form_instance = get_form_info(name)
            self._forms[name] = build_form(form_instance)
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

