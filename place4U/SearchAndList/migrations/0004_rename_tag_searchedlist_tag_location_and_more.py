# Generated by Django 5.1.dev20231109130319 on 2023-11-22 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SearchAndList', '0003_remove_searchedlist_location_alter_searchedlist_tag_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='searchedlist',
            old_name='Tag',
            new_name='tag_location',
        ),
        migrations.RemoveField(
            model_name='searchedlist',
            name='location',
        ),
    ]
