
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,student,teacher

class studentSignUpForm(UserCreationForm):
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
