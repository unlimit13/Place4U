# Generated by Django 5.1.dev20231109130319 on 2023-11-22 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SearchAndList', '0008_alter_searchedlist_tag'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='searchedtag',
            name='tag&location_set',
        ),
        migrations.RenameField(
            model_name='searchedtag',
            old_name='searchedLocation',
            new_name='searchedLocation_text',
        ),
        migrations.AddConstraint(
            model_name='searchedtag',
            constraint=models.UniqueConstraint(fields=('searchedTag_text', 'searchedLocation_text'), name='tag&location_set'),
        ),
    ]
