from django.shortcuts import render,HttpResponse,redirect
from .models import Employee,Role,Department
from datetime import datetime 
from django.db.models import Q
def index(request):
    
    return render(request,'index.html')

def all_emp(request):
    emps=Employee.objects.all()
    e={
        'emps':emps
    }
    print(emps)
    return render(request,"allemploye.html",e)

def add_emp(request):
    if request.method=='POST':
        First_name=request.POST['fname']
        Last_name=request.POST['lname']
        phone=int(request.POST['phone'])
        dept=int(request.POST.get('dept'))
        salary=int(request.POST['salary'])
        role=int(request.POST['role'])
        bonus=int(request.POST['bonus'])
        print(dept,"<================")
        print(type(dept),"<================")
        new_emp=Employee()
        new_emp.first_name=First_name
        new_emp.last_name=Last_name
        new_emp.phone=phone
        new_emp.dept_id=dept
        new_emp.salary=salary
        new_emp.role_id=role
        new_emp.bonus_id=bonus
        new_emp.hire_date=datetime.now()
        
        new_emp.save()
        return HttpResponse("Employe added succesfully")

    return render(request,'addemploye.html')

def remove_emp(request,pk=None):
    if pk:
        try:
            remove_emp= Employee.objects.get(id=pk)
            remove_emp.delete()
            # return redirect('/remove')
            return HttpResponse("Employee Remove Successfully!")
        except:
            return HttpResponse('PLEASE ENTER A VALID EMP ID')
    emp=Employee.objects.all()
    return render(request,"removeemploye.html",{'emp':emp})
def filter_emp(request):
    if request.method=='POST':
        name=request.POST.get('name')
        dept=request.POST.get('dept')
        role=request.POST.get('role')
        # emp=Employee.objects.all()
        # emps=emp
        if name:
            emps=Employee.objects.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps=Employee.objects.filter(dept__name__icontains=dept)
        if role:
            emps=Employee.objects.filter(role__name__icontains=role)
        context={
            'emps':emps
        }
        return render(request,'allemploye.html',context)
    return render(request,'filteremploye.html')
def remove_emp1(request):    
    emp=Employee.objects.all()
    return render(request,"removeemploye.html",{'emp':emp})