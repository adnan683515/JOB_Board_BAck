# Generated by Django 5.0.6 on 2024-09-16 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_our_leaders_descriptions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='our_leaders',
            old_name='position',
            new_name='title',
        ),
    ]