from django.urls import path, include
from . import views 
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employees',views.EmployeeViewSet,basename='employees')


urlpatterns = [
   path('students',views.studentsView),
   path('students/<int:pk>',views.studentDetailview),


   # path('employees/',views.Employees.as_view()), # class based view we need to write as_view() to tell that its a class-based view j
   # path('employees/<int:pk>/',views.EmployeeDetail.as_view()),

   path('',include(router.urls)),

   path('blogs/',views.BlogsView.as_view()),
   path('comments/',views.CommentView.as_view()),
]









