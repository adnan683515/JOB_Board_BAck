# Generated by Django 5.0.6 on 2024-09-13 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0003_remove_apply_box_apply_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='status',
            field=models.CharField(blank=True, choices=[('Pendding', 'Pendding'), ('Accepted', 'Accepted')], max_length=100, null=True),
        ),
    ]
