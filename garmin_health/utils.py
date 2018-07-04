# -*- coding: utf-8 -*-
"""Define generic functions to Python Garmin Health."""
from datetime import datetime, timedelta


def timestamp_calculator(nro_days_ago=1):
    "Return the timestamp in seconds from a date interval."
    now = datetime.utcnow()
    start_time = int((now - timedelta(days=nro_days_ago)).timestamp())
    end_time = int(now.timestamp())
    return start_time, end_time
