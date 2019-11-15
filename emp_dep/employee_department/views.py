from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Employee
from .serializers import EmployeeSerializer, DepartmentSerializer
import pdb
from django.db.models import Q

# Create your views here.

class EmployeeView(APIView):    
    def get(self, request, pk=None):
        dept_id = request.GET.get('dept_id', None)
        start_sal = request.GET.get('start_sal', None)
        end_sal = request.GET.get('end_sal', None)
        if pk:
            employee = get_object_or_404(Employee.objects.all(), pk=pk)
            serializer = EmployeeSerializer(employee)
        elif dept_id and start_sal and end_sal:
            employees = Employee.objects.filter(
            Q(department=int(dept_id)) & Q(salary__range=(float(start_sal), float(end_sal)))
            )
            serializer = EmployeeSerializer(employees, many=True)
        else:
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
        return Response({"employees": serializer.data})

    def post(self, request):
        employee = request.data.get('employee')
        serializer = EmployeeSerializer(data=employee)
        if serializer.is_valid(raise_exception=True):
            employee_saved = serializer.save()
        return Response({"success": "Employee '{}' created successfully".format(employee_saved.name)})

    def put(self, request, pk):
        employee = get_object_or_404(Employee.objects.all(), pk=pk)
        data = request.data.get('employee')
        serializer = EmployeeSerializer(instance=employee, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            employee_saved = serializer.save()
        return Response({"success": "Employee '{}' updated successfully".format(employee_saved.name)})

    def delete(self, request, pk):
        employee = get_object_or_404(Employee.objects.all(), pk=pk)
        employee.delete()
        return Response({"message": "Employee with id `{}` has been deleted.".format(pk)}, status=204)



