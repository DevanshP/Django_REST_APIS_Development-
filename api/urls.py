from django.urls import path, include
from . import views 



urlpatterns = [
   path('students',views.studentsView),
   path('students/<int:pk>',views.studentDetailview),
   path('employees/',views.Employees.as_view()) # class based view we need to write as_view() to tell that its a class-based view j
]










