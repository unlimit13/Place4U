# Generated by Django 5.1.dev20231109130319 on 2023-11-22 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SearchAndList', '0010_alter_searchedlist_tag'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='searchedtag',
            name='tag&location_set',
        ),
    ]