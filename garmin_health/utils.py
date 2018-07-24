# -*- coding: utf-8 -*-
"""Define generic functions to Python Garmin Health."""
import json
from datetime import datetime, timedelta


def timestamp_calculator(nro_days_ago=1):
    "Return the timestamp in seconds from a date interval."
    now = datetime.utcnow()
    start_time = int((now - timedelta(days=nro_days_ago)).timestamp())
    end_time = int(now.timestamp())
    return start_time, end_time

def save_json_data(data, filename):
    """Save JSON data to a given filename."""
    try:
        with open(filename, "w") as file:
            file.write(json.dumps(data, indent=4))
    except IOError:
        raise