from django.core.exceptions import PermissionDenied

def student_required(function):
    def wrap(request):
        if request.user.is_student == True: #checking if the user is a student
            return function(request)
        else:
            raise PermissionDenied         #Direct function which can be included. gives out an exception
    return wrap

def teacher_required(function):
    def wrap(request):
        if request.user.is_teacher == True:
            return function(request)
        else:
            raise PermissionDenied
    return wrap
