# from django.shortcuts import render
# from django.http import JsonResponse
from employee_app.models import Employee
from students.models import Student
from .serializers import EmployeeSerializer, StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404  

# def studentsView(request):
#     students = Student.objects.all()
#     students_list = list(students.values()) #Manual serilization 
#     return JsonResponse(students_list,safe=False)


#function baesed view s
@api_view(['GET','POST'])
def studentsView(request):
    if request.method == 'GET':
        #get all data from student table 
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def studentDetailview(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#class based views 

class Employees(APIView):
    def get(self,request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetail(APIView):
    def get_object(self,pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404
        
    def get(self,request,pk): 
        employee = self.get_object(pk)      #self we are calling the function inside the Employee Detail class 
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee,data=request.data) # we need to pass the employee bcuz we need which employee to update the data 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





