# grafana-awssms
A django project for sending grafana alert via AWS SMS.

## Archive Notes

We have better choices these days, starlette is my new toy~ So archive this one~

## Preparation

* Running grafana behind nginx by following http://docs.grafana.org/installation/behind_proxy/
* Create API token by following http://docs.grafana.org/http_api/auth/#create-api-token
  * Remember to keep your api key safely.

## How to use this app

If you are familiar with deploying a django project, please go ahead to use this repo directly.
Alternatively, you can pull a prebuild image from docker.
```
sudo docker pull greggu/grafana-awssms
```

Then running following command to start.
```
sudo docker run -p 8700:8700 greggu/grafana-awssms python manage.py runserver 0.0.0.0:8700
```

After that you can open http://127.0.0.1:8700 in your browser.

1. Login with admin/grafana@awssms.
2. Open Home › Backend › AWS credentials to save your AWS credential in this app.
3. Open Home › Backend › Grafana services to add a grafana service.
  * Grafana Server URL is something like http://grafana.corp.contoso.com/
  * Token is something like eyJrIjoiZVR5NGhuZDNxZ1NCeGFqT2JicDFITXlFNjhPcHluRTUiLCJuIjoidmlld2VyIiwiaWQiOjF9, you get this token from preparation step.
4. Check the grafana service that is added in step 3, select "Load rules from selected grafana services" in action list, then click GO button.
5. Open Home › Backend › Subscribers, create some users that alerts should be delivered to.
6. Open Home › Backend › Rules, there should be some rules listed. Otherwise, you should create alert rules in grafana.
7. Open one rule, add some subscribers into subscribers list.

## How to use this app in grafana

Please follow http://docs.grafana.org/alerting/notifications/#notification-channel-setup to setup a notification channel.


# TODO
Need to find a way deploy this app via gunicorn/nginx with docker.
