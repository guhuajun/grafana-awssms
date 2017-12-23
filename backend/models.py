# -*- encoding: utf-8 -*-
# pylint: disable=


from django.db import models


class GrafanaService(models.Model):

    url = models.CharField(max_length=80, verbose_name='Grafana Server URL')
    token = models.CharField(max_length=120, verbose_name='Token')

    def __str__(self):
        return self.url


class Subscriber(models.Model):

    name = models.CharField(max_length=40, verbose_name='Name')
    mobile = models.CharField(max_length=20, verbose_name='Mobile')

    def __str__(self):
        return self.name


class Rule(models.Model):

    rule_id = models.PositiveIntegerField(verbose_name='Rule Id', default=0)
    dashboard_id = models.PositiveIntegerField(verbose_name='Dashboard Id', default=0)
    panel_id = models.PositiveIntegerField(verbose_name='Panel Id', default=0)
    name = models.CharField(max_length=120, verbose_name='Name', default='')
    subscribers = models.ManyToManyField(Subscriber, verbose_name='Subscribers')

    def __str__(self):
        return self.name
