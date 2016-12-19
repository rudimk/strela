from app import *
import json


def test_timezones_endpoint_response_length():
    response = allTimeZones()
    assert len(json.loads(response.data)) == 421


