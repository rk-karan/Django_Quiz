from django.core.exceptions import PermissionDenied

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
