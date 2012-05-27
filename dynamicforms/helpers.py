# -*- coding: utf-8 -*-
from dynamicforms.exceptions import FormDoesNotExist

def get_form_info(form_name):
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

