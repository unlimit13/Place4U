# Generated by Django 5.1.dev20231109130319 on 2023-11-22 09:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='searchedTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searchedTag_text', models.CharField(max_length=200)),
                ('searchedLocation_text', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='searchedList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=3000)),
                ('likes', models.IntegerField(default=0)),
                ('place', models.CharField(max_length=200)),
                ('Tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SearchAndList.searchedtag')),
            ],
        ),
    ]
