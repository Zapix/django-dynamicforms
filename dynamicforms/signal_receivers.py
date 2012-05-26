# -*- coding: utf-8 -*-
from django.dispatch import receiver
from django.db.models.signals import post_save

from dynamicforms.models import DynamicForm
from dynamicforms import forms


@receiver(post_save, sender=DynamicForm)
def dynamic_form_post_save_handler(sender, instance, created, **kwargs):
    '''
    If it's not new form. update it
    '''
    if not created:
        forms._clear(instance.name)

