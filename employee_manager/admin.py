# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Department, Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_filter = ['department']
    list_display = ('name', 'email', 'department')


admin.site.register(Department)
admin.site.register(Employee, EmployeeAdmin)
