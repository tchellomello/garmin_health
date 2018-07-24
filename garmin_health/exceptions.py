# -*- coding: utf-8 -*-
"""Exceptions module for Python Garmin Health."""
import logging

_LOGGER = logging.getLogger(__name__)


class GarminHealthFatalException(Exception):
    """Garmin Health Fatal Exception."""
    pass
