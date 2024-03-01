from django.db import models


class Answer(models.Model):
    name = models.CharField(max_length=200)


class Question(models.Model):
    name = models.CharField(max_length=500)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)


class Test(models.Model):
    name = models.CharField(max_length=500)
    answer = models.ForeignKey(Question, on_delete=models.CASCADE)


class Student(models.Model):
    name = models.CharField(max_length=200)
    test = models.ManyToManyField(Test)
