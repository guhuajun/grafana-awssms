# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-23 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GrafanaService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=80, verbose_name='Grafana Server URL')),
                ('token', models.CharField(max_length=120, verbose_name='Token')),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule_id', models.PositiveIntegerField(verbose_name='Rule ID')),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('mobile', models.CharField(max_length=20, verbose_name='Mobile')),
            ],
        ),
        migrations.AddField(
            model_name='rule',
            name='subscribers',
            field=models.ManyToManyField(to='backend.Subscriber', verbose_name='Subscribers'),
        ),
    ]