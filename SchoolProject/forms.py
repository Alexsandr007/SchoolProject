from django import forms
from .models import *


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['test', 'text']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'is_correct']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'school_class']
