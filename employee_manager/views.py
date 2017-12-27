# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponseBadRequest
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from .models import Employee, Department
from django.db.models import F


def index(request):
    if request.method == 'GET':
        employees = Employee.objects.values('name', 'email').annotate(department=F('department__name'))
        return JsonResponse(list(employees), safe=False)
    elif request.method == 'POST':
        return post(request)

    return HttpResponseBadRequest()


def post(request):
    try:
        department = Department.objects.get(name=request.POST['department'])
        Employee.objects.create(name=request.POST['name'], email=request.POST['email'], department=department)
    except Department.DoesNotExist:
        return JsonResponse({
            'message': 'Department does not exist.'
        }, status=400)
    except IntegrityError:
        return JsonResponse({
            'message': 'This email already exists.'
        }, status=400)
    return JsonResponse(request.POST)


def delete(request, employee_id):
    if request.method == 'DELETE':
        employee = get_object_or_404(Employee, pk=employee_id)
        employee.delete()
        return JsonResponse({
            'message': 'Employee was been deleted.'
        }, safe=False)

    return JsonResponse({
        'message': 'Employee does not exist.'
    }, status=404)

