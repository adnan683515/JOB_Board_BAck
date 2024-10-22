# Generated by Django 5.0.6 on 2024-09-20 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_browse_cetagory_slug_organizationtype_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='work_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
