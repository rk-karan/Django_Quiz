from django.core.exceptions import PermissionDenied
from .models import quiz_info, Quiz
from django.shortcuts import get_object_or_404

def teacher_quiz_required(function):
    def wrap(request, quiz_pk, question_pk):
        if request.user.is_authenticated == True and request.user.is_teacher == True:
            return function(request, quiz_pk, question_pk)
        else:
            raise PermissionDenied
    return wrap
    
def quiz_access(function):
    def wrap(request, pk):
        if request.user.is_authenticated == True:
            if request.user.is_teacher:
                return function(request, pk)
            else:
                quiz=get_object_or_404(Quiz, pk=pk)
                info=quiz_info.objects.all().filter(student=request.user, quiz=quiz)
                if info.exists():
                    return function(request, pk)
                else:
                    raise PermissionDenied
        else:
            raise PermissionDenied
    return wrap

def student_required(function):
    def wrap(request, pk):
        if request.user.is_authenticated == True and request.user.is_student == True: #checking if the user is a student
            return function(request, pk)
        else:
            raise PermissionDenied         #Direct function which can be included. gives out an exception
    return wrap

def teacher_required(function):
    def wrap(request, pk):
        if request.user.is_authenticated == True and request.user.is_teacher == True:
            return function(request, pk)
        else:
            raise PermissionDenied
    return wrap

def teacher_login(function):
    def wrap(request):
        if request.user.is_authenticated == True and request.user.is_teacher == True:
            return function(request)
        else:
            raise PermissionDenied
    return wrap

def student_login(function):
    def wrap(request):
        if request.user.is_authenticated == True and request.user.is_student == True: #checking if the user is a student
            return function(request)
        else:
            raise PermissionDenied         #Direct function which can be included. gives out an exception
    return wrap
