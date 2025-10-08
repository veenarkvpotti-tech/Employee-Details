from django.shortcuts import render,redirect
from .forms import EmployeeForm

from .models import Employee


def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

def edit_employee(request, id):
    
    employee= Employee.objects.filter(id=id)

    if not employee.exists():  
        return redirect('employee_list')
    
    employee = employee.first()  

    

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'edit_employee.html', {'form': form})



def delete_employee(request, id):
    employee = Employee.objects.filter(id=id)
    if employee.exists():
     employee.delete()
    return redirect('employee_list')
