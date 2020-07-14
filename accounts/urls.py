from django.urls import path, include
from . import views

urlpatterns = [
#registration portal for students
    path('signup_as_teacher', views.signup_as_teacher.as_view(), name='signup_as_teacher'),

#registration portal for teachers
    path('signup_as_student', views.signup_as_student.as_view(), name='signup_as_student'),

#signin page
    path('signin', views.signin, name='signin'),

#signout
    path('signout', views.signout, name='signout'),

#once teacher registration is successful, take to teacher home
    path('teacher_home', views.teacher_home, name='teacher_home'),

#once student registration is successful, take to student home
    path('student_home', views.student_home, name='student_home'),

#for creating quizzes by teachers
    path('create_quiz', views.create, name='create_quiz'),

#for viewing quiz after it is created
    path('quiz_view/<int:pk>', views.quiz_view, name='quiz_view'),

#for adding questions
    path('add_questions/<int:pk>', views.add_questions, name='add_question'),

#for adding answers
    path('add_answers/<int:quiz_pk>/<int:question_pk>', views.add_answers, name='add_answers'),

#for students viewing quizzes
    path('student_quiz_view/<int:quiz_pk>', views.student_quiz_view, name='student_quiz_view'),

#for students attempting quiz
    path('question_view/<int:quiz_pk>/<int:num>', views.question_view, name='question_view'),

#for caculating score after answer submitted
    path('calculate/<int:quiz_pk>/<int:question_pk>/<int:num>', views.calculate, name='calculate'),

#for calculating final score
#    path('final_score/<int:quiz_pk>', views.final_score, name='final_score'),
]
