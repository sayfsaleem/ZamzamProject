# Generated by Django 4.2.6 on 2023-10-31 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_teacher_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_image',
            field=models.ImageField(upload_to='students'),
        ),
    ]
