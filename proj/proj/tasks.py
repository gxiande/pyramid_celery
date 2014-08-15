__author__ = 'json'
from celery.task import task

@task
def add(x, y):
    print x+y