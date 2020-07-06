from django.contrib import admin
from .models import User, student, teacher

admin.site.register(User)
admin.site.register(student)
admin.site.register(teacher)
