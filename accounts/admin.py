from django.contrib import admin
from .models import User, student, teacher, Quiz, questions, answers, question_info

admin.site.register(User)
admin.site.register(student)
admin.site.register(teacher)
admin.site.register(Quiz)
admin.site.register(questions)
admin.site.register(answers)
admin.site.register(question_info)
