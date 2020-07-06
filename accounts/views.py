from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import studentSignUpForm, teacherSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User

def home(request):
    return render(request, 'accounts/home.html')

class signup_as_student(CreateView):
    model = User
    form_class = studentSignUpForm
    template_name = 'accounts/signup_as_student.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/accounts/student_home')

class signup_as_teacher(CreateView):
    model = User
    form_class = teacherSignUpForm
    template_name = 'accounts/signup_as_teacher.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/accounts/teacher_home')

def signin(request):
    return render(request, 'accounts/signin.html')

def signout(request):
    return render(request, 'accounts/home.html')

def teacher_home(request):
    return render(request, 'accounts/teacher_home.html')

def student_home(request):
    return render(request, 'accounts/student_home.html')
