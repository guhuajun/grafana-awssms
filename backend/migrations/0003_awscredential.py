# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-23 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20171223_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='AwsCredential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_key', models.CharField(max_length=80, verbose_name='Access Key')),
                ('secret_key', models.CharField(max_length=80, verbose_name='Secret Key')),
            ],
        ),
    ]
