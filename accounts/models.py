from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)

class student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Quiz(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')
    topic = models.CharField(max_length = 150)
    quiz_name=models.CharField(max_length=150)
    max_marks = models.IntegerField()
    number_of_questions = models.IntegerField()

class questions(models.Model):
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question=models.TextField()
    marks=models.IntegerField()

class answers(models.Model):
    question=models.ForeignKey(questions, on_delete=models.CASCADE, related_name='answers')
    text=models.CharField(max_length=255)
    is_correct=models.BooleanField('Correct answer', default=False)
