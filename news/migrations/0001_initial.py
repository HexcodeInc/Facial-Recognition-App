# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-26 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='game_Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_header', models.CharField(max_length=20)),
                ('news_brief', models.CharField(max_length=50)),
                ('news_link', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='politics_Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_header', models.CharField(max_length=20)),
                ('news_brief', models.CharField(max_length=50)),
                ('news_link', models.CharField(max_length=40)),
            ],
        ),
    ]
