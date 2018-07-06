# -*- coding: utf-8 -*-
"""Define constants used by Python Garmin Health."""

# Garmin Health Connection API
API_URL = "https://healthapi.garmin.com/wellness-api/rest"
ACCESS_TOKEN_URL = \
    "https://connectapi.garmin.com/oauth-service/oauth/access_token"
AUTHORIZE_TOKEN_URL = "https://connect.garmin.com/oauthConfirm"
REQUEST_TOKEN_URL = \
    "https://connectapi.garmin.com/oauth-service/oauth/request_token"

# Garmin Health Connection API Data Endpoints
API_DAILIES = "{0}/dailies?".format(API_URL)
API_ACTIVITIES = "{0}/activities?".format(API_URL)
API_SLEEPS = "{0}/sleeps?".format(API_URL)
API_BODY = "{0}/bodyComps?".format(API_URL)
API_STRESS = "{0}/stressDetails?".format(API_URL)
API_USER_METRICS = "{0}/userMetrics?".format(API_URL)
API_MOVEIQ = "{0}/moveiq?".format(API_URL)
API_USER_ID = "{0}/user/id".format(API_URL)


# Garmin Health Constants
RETRY = 3

CONFIG_DATA = {
    'client_key': None,
    'client_secret': None,
    'resource_owner_key': None,
    'resource_owner_secret': None,
    'verifier': None,
}
