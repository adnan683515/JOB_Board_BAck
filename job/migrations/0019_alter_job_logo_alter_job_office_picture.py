# Generated by Django 5.0.6 on 2024-10-01 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0018_remove_job_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='logo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='office_picture',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
