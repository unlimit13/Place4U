# Generated by Django 5.1.dev20231109130319 on 2023-11-22 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SearchAndList', '0004_alter_searchedtag_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='searchedtag',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='searchedtag',
            constraint=models.UniqueConstraint(fields=('searchedTag_text', 'searchedLocation'), name='tag&location set'),
        ),
    ]
