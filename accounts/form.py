from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,student,teacher, Quiz, questions, answers

class studentSignUpForm(UserCreationForm):
    #can be added
    #first_name = forms.CharField(required=True)
    #last_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        #we are using our user authentication model named User
        model = User

    @transaction.atomic   #helps us to comit changes in the database
    def save(self):
        user = super().save(commit=False)  #commit is set to false intially so that the user first name
                                           #and second name can be cleaned first and then saved.
        user.is_student = True
        #can be added
        #user.first_name = self.cleaned_data.get('first_name')
        #user.last_name = self.cleaned_data.get('last_name')
        user.save()
        Student = student.objects.create(user=user)
        Student.save()
        return user

class teacherSignUpForm(UserCreationForm):
    #can be added
    #first_name = forms.CharField(required=True)
    #last_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        #we are using our user authentication model named User
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.is_staff = True
        #can be added
        #user.first_name = self.cleaned_data.get('first_name')
        #user.last_name = self.cleaned_data.get('last_name')
        user.save()
        Teacher = teacher.objects.create(user=user)
        Teacher.save()
        return user

class create_quiz(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('quiz_name', 'topic', 'max_marks', 'number_of_questions' )

class add_question_form(forms.ModelForm):
    class Meta:
        model=questions
        fields=('question', 'marks')

class add_answers_form(forms.ModelForm):
    class Meta:
        model=answers
        fields=('text', 'is_correct')
