# -*- coding: utf-8 -*-
from django.contrib import admin

from dynamicforms import models


class DynamicFieldInline(admin.TabularInline):
    model = models.DynamicField


class DynamicFormAdmin(admin.ModelAdmin):
    inlines = [DynamicFieldInline]


admin.site.register(models.DynamicForm, DynamicFormAdmin)

