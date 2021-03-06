# Generated by Django 3.0.8 on 2020-07-09 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=150)),
                ('quiz_name', models.CharField(max_length=150)),
                ('max_marks', models.IntegerField()),
                ('number_of_questions', models.IntegerField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
