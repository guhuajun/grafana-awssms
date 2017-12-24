# -*- encoding: utf-8 -*-
# pylint: disable=

import logging
from concurrent.futures import ThreadPoolExecutor

import boto3
import simplejson as json
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response

from backend import models


class AlertHandlerView(APIView):
    '''
    Handler for processing alerts from grafana
    Reference: http://docs.grafana.org/alerting/notifications/#webhook
    '''

    authentication_classes = (authentication.BasicAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        logger = logging.getLogger('backend')

        # get aws credential
        cred = models.AwsCredential.objects.first()
        aws_client = boto3.client(
            'sns',
            region_name='us-east-1',
            aws_access_key_id=cred.access_key,
            aws_secret_access_key=cred.secret_key
        )

        def send_sms(phone, message):
            response = aws_client.publish(
                PhoneNumber=phone,
                Message=message
            )
            logger.debug(response)

        try:
            alert = json.loads(request.body)
            rule_id = alert['ruleId']

            if alert['state'] != 'ok':
                rule = models.Rule.objects.filter(
                    rule_id=rule_id).first()
                if rule:
                    with ThreadPoolExecutor(max_workers=4) as worker:
                        for subscriber in rule.subscribers.all():
                            worker.submit(send_sms, subscriber, alert['message'])

            return Response(data={'status': 'ok'})
        except Exception as ex:
            logger.error(ex)
            return Response(data={'exception': str(ex)}, status=500)
