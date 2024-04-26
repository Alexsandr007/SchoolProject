from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.TextField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)


class SchoolClass(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200)
    test = models.ManyToManyField(Test, null=True, blank=True)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.name