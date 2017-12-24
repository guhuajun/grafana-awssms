# -*- encoding: utf-8 -*-
# pylint: disable=

from django.conf.urls import url

from backend import views

urlpatterns = [
    url(r'alerthandler', views.AlertHandlerView.as_view(), name='alerthandler'),
]
