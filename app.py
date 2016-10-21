from flask import Flask, request, Response
import arrow
import json
from timezones import timezones
import collections

app = Flask(__name__)

@app.route('/timezones')
def allTimeZones():
    timezone_list = json.dumps(timezones)
    resp = Response(timezone_list, status=200, mimetype='application/json')
    return resp

@app.route('/timezones/convert')
def convertUtcToTimeZone():
    timezone_id = int(request.args.get('timezone_id'))
    for tz in timezones:
        if tz['timezone_id'] == timezone_id:
            timezone_name = tz['timezone_name']
    utc_time = arrow.utcnow()
    local_time = utc_time.to(timezone_name)
    payload = collections.OrderedDict()
    payload['utc'] = utc_time.format('MM-DD-YYYY HH:mm:SS Z')
    payload[timezone_name.lower()] = local_time.format('MM-DD-YYYY HH:mm:SS Z')
    payload['format'] = 'MM-DD-YYYY HH:mm:SS Z'
    resp = Response(json.dumps(payload), status=200, mimetype='application/json')
    return resp



if __name__ == '__main__':
    app.run(port=8080, debug=True)