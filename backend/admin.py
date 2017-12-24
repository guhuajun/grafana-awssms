# -*- encoding: utf-8 -*-
# pylint: disable=

import requests
import simplejson as json
from django.contrib import admin
from django.contrib import messages

from backend import models


class GrafanaServiceAdmin(admin.ModelAdmin):

    actions = ['test_service', 'load_rules']

    def test_service(self, request, queryset):
        for service in queryset.all():
            url = service.url if service.url.endswith('/') else service.url + '/'
            url = url + 'api/alerts/'
            headers = {
                'Authorization': 'Bearer ' + service.token
            }

            total_rules = 0
            try:
                response = requests.get(url, headers=headers)
                json_response = json.loads(response.content)
                total_rules = len(json_response)
                self.message_user(request, '{0} is verified, found {1} rules.'.format(url, total_rules))
            except Exception as ex:
                self.message_user(request, 'Failed to verify {0}'.format(url), level=messages.ERROR)
    test_service.short_description = 'Test selected grafana services'

    def load_rules(self, request, queryset):
        for service in queryset.all():
            url = service.url if service.url.endswith('/') else service.url + '/'
            url = url + 'api/alerts/'
            headers = {
                'Authorization': 'Bearer ' + service.token
            }

            try:
                response = requests.get(url, headers=headers)
                json_response = json.loads(response.content)
                rules = json_response
                for rule in rules:
                    defaults = {
                        "dashboard_id": rule['dashboardId'],
                        "panel_id": rule['panelId'],
                        "name": rule['name']
                    }
                    models.Rule.objects.get_or_create(
                        service=service,
                        rule_id=rule['id'],
                        defaults=defaults
                    )
                self.message_user(request, '{0} rules are loaded.'.format(len(rules)))
            except Exception as ex:
                self.message_user(request, 'Failed to loads rules from {0}, {1}'.format(
                    url, str(ex)), level=messages.ERROR)
    load_rules.short_description = 'Load rules from selected grafana services'


admin.site.register(models.GrafanaService, GrafanaServiceAdmin)
admin.site.register(models.AwsCredential)
admin.site.register(models.Subscriber)
admin.site.register(models.Rule)


admin.site.site_header = 'Grafana AWS SMS'
admin.site.site_title = 'Grafana AWS SMS'
admin.site.index_title = 'Grafana AWS SMS'