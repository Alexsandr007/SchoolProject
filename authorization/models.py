from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import models
from SchoolProject.models import Student
from django.contrib.auth.models import User


class UserManager(BaseUserManager):
    def authenticate(self, request, username=None, password=None):
        try:
            teacher = Teacher.objects.get(username=username)
            if teacher.password == password:
                return teacher
        except self.model.DoesNotExist:
            return None

    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')
        if not password:
            raise ValueError('The Password field must be set')

        teacher = self.model(
            username=self.normalize_username(username),
            email=self.normalize_email(email),
        )
        teacher.set_password(password)
        teacher.save(using=self._db)
        return teacher

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class School(models.Model):
    name = models.CharField(max_length=150, unique=True)
    address = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Teacher(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def clean(self):
        super().clean()
        validate_email(self.email)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)