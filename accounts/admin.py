from django.contrib import admin
from .models import User, student, teacher, Quiz, questions, answers

admin.site.register(User)
admin.site.register(student)
admin.site.register(teacher)
admin.site.register(Quiz)
admin.site.register(questions)
admin.site.register(answers)
