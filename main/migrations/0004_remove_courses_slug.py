# Generated by Django 4.0.2 on 2023-10-26 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_courses_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='slug',
        ),
    ]
