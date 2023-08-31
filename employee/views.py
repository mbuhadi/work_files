from django.shortcuts import render
from employee.models import Employee
from rest_framework.generics import ListCreateAPIView
from .serializers import EmployeeSerializer
from rest_framework import permissions

class EmployeeListCreate(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        queryset = Employee.objects.all()
        return queryset