# Generated by Django 5.0.6 on 2024-09-20 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0014_job_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created_on',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
