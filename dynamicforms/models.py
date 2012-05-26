from django.db import models

from django.utils.translation import ugettext_lazy as _

from dynamicforms.utils import get_choices_field_list


class DynamicForm(models.Model):
    '''
    Model for building forms.
    '''
    name = models.CharField(
               max_length=30,
               verbose_name=_('Form name'),
               help_text=_('Only in English and in camel notation'),
               unique=True)
    description = models.TextField(verbose_name=_('Form description'),
                                   blank=True, null=True)

    class Meta:
        verbose_name = _('Dynamic Form')
        verbose_name_plural = _('Dynamic Forms')

    def __unicode__(self):
        return unicode(self.name)


class DynamicField(models.Model):
    '''
    Describing field for Dynamic class
    '''
    form = models.ForeignKey(DynamicForm, related_name='fields')
    field = models.CharField(max_length=250, verbose_name=_('Form field'),
                             choices=get_choices_field_list())
    field_name = models.CharField(
                     max_length=250,
                     verbose_name=_('Field name'),
                     help_text=_('Only in English and in lowercase'))
    label = models.CharField(max_length=250, verbose_name=_('Label'))
    help_text = models.TextField(verbose_name=_('Help text'), blank=True)

    class Meta:
        verbose_name = _('Dynamic field')
        verbose_name_plural = _('Dynamic fields')

    def __unicode__(self):
        return u'%s(%s)' % (self.field_name, self.field)

from dynamicforms import signal_receivers
