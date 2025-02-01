from django.db import models
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()


class Student(models.Model):
    studentname = models.CharField(max_length=80)
    studentage = models.IntegerField()