# Generated by Django 5.1.dev20231109130319 on 2023-11-22 08:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SearchAndList', '0007_remove_searchedtag_tag_location_set_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchedlist',
            name='Tag',
            field=models.ForeignKey(db_column='searchedTag_text', on_delete=django.db.models.deletion.CASCADE, to='SearchAndList.searchedtag'),
        ),
    ]
