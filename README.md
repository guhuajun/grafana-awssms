# grafana-awssms
A django project for sending grafana alert via AWS SMS.

# Preparation

* Running grafana behind nginx by following http://docs.grafana.org/installation/behind_proxy/
* Create API token by following http://docs.grafana.org/http_api/auth/#create-api-token
  * Remember to keep your api key safely.

# How to use this app

If you are familiar with deploying a django project, please go ahead to use this repo directly.
Alternatively, you can pull a prebuild image from docker.
```
sudo docker pull greggu/grafana-awssms
```

Then running following command to start.
```
sudo docker run greggu/grafana-awssms gunicorn project.wsgi:application -b 0.0.0.0:8700
```
