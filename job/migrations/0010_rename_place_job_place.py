# Generated by Django 5.0.6 on 2024-09-14 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_company_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='place',
            new_name='Place',
        ),
    ]