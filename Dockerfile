FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN python manage.py migrate
RUN python manage.py collectstatic --no-input
RUN echo "from django.contrib.auth.models import User; User.objects.filter(email='admin@localhost').delete(); User.objects.create_superuser('admin', 'admin@localhost', 'grafana@awssms')" | python manage.py shell
