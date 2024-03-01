from django.contrib import admin
from .models import *


class StudentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.fields]


class TestAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Test._meta.fields]


class QuestionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Question._meta.fields]


class AnswerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Answer._meta.fields]


admin.site.register(Student, StudentAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
