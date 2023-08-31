from rest_framework import serializers
from .models import Employee
from django.core.validators import RegexValidator

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = (
            "id",
            "name_ar",
            "name_en",
            'file_id',
            'finger_print_id',
            'national_id',
            'department',
        )