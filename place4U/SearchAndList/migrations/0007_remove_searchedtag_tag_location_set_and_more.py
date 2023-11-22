# Generated by Django 5.1.dev20231109130319 on 2023-11-22 08:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SearchAndList', '0006_remove_searchedtag_id_alter_searchedlist_tag_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='searchedtag',
            name='tag&location set',
        ),
        migrations.AlterField(
            model_name='searchedlist',
            name='Tag',
            field=models.ForeignKey(db_column='tag&location_set', on_delete=django.db.models.deletion.CASCADE, to='SearchAndList.searchedtag'),
        ),
        migrations.AddConstraint(
            model_name='searchedtag',
            constraint=models.UniqueConstraint(fields=('searchedTag_text', 'searchedLocation'), name='tag&location_set'),
        ),
    ]