from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views.generic import CreateView
from .form import studentSignUpForm, teacherSignUpForm, create_quiz, add_question_form, add_answers_form
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Quiz, questions, answers

from .decorators import student_required, teacher_required, student_login, teacher_login, teacher_quiz_required

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

def quiz_view(request, pk):
    quiz = get_object_or_404(Quiz, pk = pk, creator = request.user)
    #added set and set as contexts to search through the libraries
    return render(request, 'accounts/quiz_view.html', context={'quiz':quiz, 'set':questions.objects.all(), 'set1':answers.objects.all()})


def signin(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): #is_valid will check if the entries are of consistent datatype (no null value accepted)
            username = form.cleaned_data.get('username') #to get cleaned username
            password = form.cleaned_data.get('password') #to get cleaned password
            user = authenticate(username=username, password=password) #we are checking if the password and username are correct
            #authenticate() returns none if password and username doesnt match
            if user is not None : #if condition
                if user.is_active:
                    login(request,user)
                    if user.is_student==True:
                        return redirect('/accounts/student_home') #to student dashboard
                    else:
                        return redirect('/accounts/teacher_home') #to teacher dashboard
                else:
                    messages.error(request,"User has been temporarily deactivated") #invalid message display
            else:
                messages.error(request,"Invalid username or password") #invalid message display
        else:
                messages.error(request,"Invalid username or password") #invalid message display
    return render(request, 'accounts/signin.html', context={'form':AuthenticationForm()})

def signout(request):
    logout(request)
    return render(request, 'accounts/home.html')

@teacher_login
def teacher_home(request):
    return render(request, 'accounts/teacher_home.html', context = {'set':Quiz.objects.all()})

@student_login
def student_home(request):
    return render(request, 'accounts/student_home.html', context = {'set':Quiz.objects.all()})

@teacher_login
def create(request):
    if request.method=='POST':
        quiz = Quiz()
        quiz.quiz_name = request.POST.get('quiz_name')
        quiz.topic = request.POST.get('topic')
        quiz.number_of_questions = request.POST.get('number_of_questions')
        quiz.max_marks = request.POST.get('max_marks')
        quiz.creator = request.user
        quiz.save()
        return redirect('/accounts/quiz_view/'+str(quiz.pk))
    return render(request, 'accounts/create_quiz.html', context={'form':create_quiz})

@teacher_required
def add_questions(request, pk):
    print("========", pk)
    quiz = get_object_or_404(Quiz, pk = pk, creator = request.user)

    if request.method=='POST':
        question = questions()
        question.question = request.POST.get('question')
        question.marks = request.POST.get('marks')
        question.quiz = quiz
        question.save()
        return redirect('/accounts/quiz_view/'+str(quiz.pk))
    return render(request, 'accounts/add_question.html', context={'form':add_question_form, 'quiz':quiz})

@teacher_quiz_required  #go to decorators.py for more info
def add_answers(request, quiz_pk, question_pk):
    print("========", quiz_pk, question_pk)
    quiz = get_object_or_404(Quiz, pk=quiz_pk, creator=request.user) #retrieving the quiz object
    question = get_object_or_404(questions, pk=question_pk, quiz=quiz) #retireving the question object

    if request.method=='POST':
        answer=answers()
        answer.text=request.POST.get('text')
        #the output given when {{form}} is saved is 'on'. But we have to save 'True/False' for boolean field
        if request.POST.get('is_correct')=='on':
            answer.is_correct=True
        else:
            answer.is_correct=False

        answer.question=question
        answer.save()
        return redirect('/accounts/quiz_view/'+str(quiz.pk))
    return render(request, 'accounts/add_answer.html', context={'form':add_answers_form, 'quiz':quiz, 'question':question})
