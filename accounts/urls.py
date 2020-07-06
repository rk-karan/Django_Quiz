from django.urls import path, include
from . import views

urlpatterns = [
    path('signup_as_teacher', views.signup_as_teacher.as_view(), name='signup_as_teacher'),
    path('signup_as_student', views.signup_as_student.as_view(), name='signup_as_student'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('teacher_home', views.teacher_home, name='teacher_home'),
    path('student_home', views.student_home, name='student_home'),
]
