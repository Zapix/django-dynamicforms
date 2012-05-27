"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.forms import Form, CharField
from dynamicforms import forms
from dynamicforms.utils import get_field_class


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_all_true(self):
        self.assertTrue([True, True, True])


def ImportTest(TestCase):
    '''
    Test sub class
    '''
    def test_import_charfield(self):
        field_class = get_field_class('django.forms.CharField')
        self.assertTrue(issubclass(field_class, CharField))


class DynamicFormTest(TestCase):
    '''
    Testing forms lazy object
    '''
    fixtures = ['test_form.json']

    def get_form_class(self):
        return forms.PeopleForm

    def test_get_class(self):
        form_class = self.get_form_class()
        self.assertTrue(issubclass(form_class, Form))

    def test_valid_data(self):
        form_class = self.get_form_class()
        form = form_class({'name': 'Zapix', 'age': 23, 'alive': True})
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form_class = self.get_form_class()
        form = form_class({'name': 'Zapix'})
        self.assertTrue(form.is_valid() == False)
