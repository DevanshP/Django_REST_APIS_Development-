from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student


def studentsView(request):
    students = Student.objects.all()
    students_list = list(students.values()) #Manual serilization 
    return JsonResponse(students_list,safe=False)





