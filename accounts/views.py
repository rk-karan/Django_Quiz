from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import studentSignUpForm, teacherSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User

def home(request):
    return render(request, 'accounts/home.html')

class signup_as_student(CreateView):  #CreateView creates an instance of the database
    model = User  #we use our abstractuser model
    form_class = studentSignUpForm  #as it is student signup, we use studentSignUpForm
    template_name = 'accounts/signup_as_student.html' #template_name

    def form_valid(self, form):
        user = form.save() #saving the information in the form in the database
        login(self.request, user) #once registration is successful, the student is logged in
        return redirect('/accounts/student_home') #redirecting to student home

class signup_as_teacher(CreateView):  #CreateView creates an instance of the database
    model = User  #we use our abstractuser model
    form_class = teacherSignUpForm  #as it is teacher signup, we use teacherSignUpForm
    template_name = 'accounts/signup_as_teacher.html' #template_name

    def form_valid(self, form):
        user = form.save()  #saving the information in the form in the database
        login(self.request, user)  #once registration is successful, the teacher is logged in
        return redirect('/accounts/teacher_home')  #redirecting to student home
        
def signin(request):
    return render(request, 'accounts/signin.html')	    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): #is_valid will check if the entries are of consistent datatype (no null value accepted)
            username = form.cleaned_data.get('username') #to get cleaned username
            password = form.cleaned_data.get('password') #to get cleaned password
            user = authenticate(username=username, password=password) #we are checking if the password and username are correct
            #authenticate() returns none if password and username doesnt match
            if user is not None : #if condition
                login(request,user)
                if user.is_student==True:
                    return redirect('/accounts/student_home') #to student dashboard
                else:
                    return redirect('/accounts/teacher_home') #to teacher dashboard
            else:
                messages.error(request,"Invalid username or password") #ivalid message display
        else:
                messages.error(request,"Invalid username or password") #ivalid message display
    return render(request, 'accounts/signin.html', context={'form':AuthenticationForm()})

def signout(request):
    logout(request)
    return render(request, 'accounts/home.html')

def teacher_home(request):
    return render(request, 'accounts/teacher_home.html')

def student_home(request):
    return render(request, 'accounts/student_home.html')
