# Generated by Django 5.0.6 on 2024-09-12 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='browse_cetagory',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='organizationtype',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]