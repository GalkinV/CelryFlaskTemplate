#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals
import os
import time

import ujson
from datetime import datetime
import logging

try:
    from worker import app

except:
    from .worker import app

from celery.utils.log import get_task_logger
from celery import shared_task

logger = get_task_logger(__name__)


# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
@shared_task(bind=True, name="queue_1:task_type_1", acks_late=True, reject_on_worker_lost=True,
             autoretry_for=(RuntimeError,), retry_kwargs={"countdown": 2, "max_retries": 3})
def run_task_1(self, delay, aoi, **param):
    logger.info(f'delay to {delay}, {aoi}, {param}')
    time.sleep(delay)
    logger.info(f'after delay {delay}, {aoi}, {param}')

    return True


# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
@shared_task(bind=True, name="queue_1:task_type_2", acks_late=True, reject_on_worker_lost=True,
             autoretry_for=(RuntimeError,), default_retry_delay=10 * 60, max_retries=146)
def run_task_2(self, args, **kwargs):
    # result = downloader(args,**kwargs)
    # if isinstance(result,(list)):
    #     return result
    # else:
    #     print("Waiting for the data")
    #     raise self.retry()
    return True
