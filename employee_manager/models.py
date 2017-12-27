# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=None, blank=False)
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(unique=True, blank=False)

    def __str__(self):
        return self.name
