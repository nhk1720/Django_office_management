from rest_framework import serializers
from empapp.models import Department,Role,Employee
class EmployeDept(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=["id","name","locations"]
class EmployeRole(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields=["id","name"]
class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=["id","first_name","last_name","dept","salary","bonus","role","phone","hire_date"]