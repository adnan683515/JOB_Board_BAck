# Generated by Django 5.0.6 on 2024-09-27 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0008_alter_apply_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='resume',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]