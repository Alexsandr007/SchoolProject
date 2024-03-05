from django.contrib import admin
from .models import Teacher,School

class SchoolAdmin(admin.ModelAdmin):
    list_display = [field.name for field in School._meta.fields]

class TeacherAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Teacher._meta.fields]


admin.site.register(School, SchoolAdmin)
admin.site.register(Teacher, TeacherAdmin)

