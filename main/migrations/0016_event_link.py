# Generated by Django 4.2.6 on 2023-11-01 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]