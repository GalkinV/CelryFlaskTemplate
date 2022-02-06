#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import os
from celery import Celery
from celery.schedules import crontab

try:
    CELERY_BROKER_URL = os.environ["CELERY_BROKER_URL"]
except:
    raise RuntimeError("CELERY_BROKER_URL not defined")
try:
    CELERY_BACKEND_URL = os.environ["CELERY_BACKEND_URL"]
except:
    CELERY_BACKEND_URL = None


app = Celery(__name__)
app.conf.update({
    "broker_url": CELERY_BROKER_URL,
    "result_backend" : CELERY_BACKEND_URL,
    "imports": (
        "tasks","task_router",
    ),
#    "worker_max_tasks_per_child":1,
    "task_routes": ("task_router.TaskRouter",),
    "task_serializer": "json",
    "result_serializer": "json",
    "accept_content": ["json"]})

app.conf.beat_schedule={
    'search-meta': {
    'task': 'scheduler:viirs',  
    'schedule': crontab(hour=0, minute=1,),
    'args': (["auto"]),
    }
}
