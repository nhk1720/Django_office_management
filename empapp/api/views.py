from empapp.api.serializer import EmployeDept,EmployeRole,EmployeSerializer
from empapp.models import Department,Role,Employee
from rest_framework import viewsets
class Emp_Dept(viewsets.ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=EmployeDept

class Role_Dept(viewsets.ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=EmployeRole
    
class Emp_Details(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeSerializer