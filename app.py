from flask import Flask, request, Response
import arrow
import json
from timezones import timezones

app = Flask(__name__)

@app.route('/timezones')
def allTimeZones():
    timezone_list = json.dumps(timezones)
    resp = Response(timezone_list, status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(port=8080, debug=True)