# Generated by Django 4.0.2 on 2023-10-26 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_courses_weeks'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='lessons',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
