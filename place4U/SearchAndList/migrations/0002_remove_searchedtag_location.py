# Generated by Django 5.1.dev20231109130319 on 2023-11-20 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SearchAndList', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchedtag',
            name='location',
        ),
    ]
