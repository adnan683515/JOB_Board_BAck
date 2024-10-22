# Generated by Django 5.0.6 on 2024-09-13 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0002_alter_apply_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='box',
        ),
        migrations.AddField(
            model_name='apply',
            name='status',
            field=models.CharField(blank=True, choices=[('Accepted', 'Accepted')], default='Pendding', max_length=100, null=True),
        ),
    ]
