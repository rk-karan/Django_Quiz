from django.urls import path, include
from . import views

urlpatterns = [
#registration portal for students
    path('signup_as_teacher', views.signup_as_teacher.as_view(), name='signup_as_teacher'),

#registration portal for teachers
    path('signup_as_student', views.signup_as_student.as_view(), name='signup_as_student'),

#signin page
    path('signin', views.signin, name='signin'),
    
#post signin page
    path('signin/done', views.signin_done, name='done'),

#signout
    path('signout', views.signout, name='signout'),

#once teacher registration is successful, take to teacher home
    path('teacher_home', views.teacher_home, name='teacher_home'),

#once student registration is successful, take to student home
    path('student_home', views.student_home, name='student_home'),
]
