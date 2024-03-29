# Generated by Django 4.1.6 on 2024-03-05 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0002_alter_teacher_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('address', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='school',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='authorization.school'),
            preserve_default=False,
        ),
    ]
