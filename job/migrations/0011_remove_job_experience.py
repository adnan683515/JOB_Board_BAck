# Generated by Django 5.0.6 on 2024-09-16 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_rename_place_job_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='experience',
        ),
    ]
