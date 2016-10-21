## Strela

This doc outlines the main endpoints exposed by the Strela API, as well as what kind of parameters they accept and the responses they return.



### Installation

To install Strela, please follow the steps below:

1. Clone Strela.
2. Install dependencies - you can create a virtualenv or install them system-wide: `pip install -r requirements.txt`
3. Run the API server using `python app.py`

If you'd like to run Strela as a long-running process, I recommend a combination of [Gunicorn](http://gunicorn.org/) and [PM2](http://pm2.keymetrics.io/) - PM2 was originally meant for Node.js but it works perfectly with Gunicorn too.

### All Timezones

This endpoint returns a list of all timezones that both Strela and the Arrow package support. The URL for this endpoint is `/timezones`. The response is like this:

```json
[
  {
    "timezone_id": 1,
    "timezone_name": "Africa/Abidjan"
  },
  {
    "timezone_id": 2,
    "timezone_name": "Africa/Accra"
  },
  {
    "timezone_id": 3,
    "timezone_name": "Africa/Addis_Ababa"
  },
  {
    "timezone_id": 4,
    "timezone_name": "Africa/Algiers"
  },
  {
    "timezone_id": 5,
    "timezone_name": "Africa/Asmara"
  },
  {
    "timezone_id": 6,
    "timezone_name": "Africa/Bamako"
  },
  {
    "timezone_id": 7,
    "timezone_name": "Africa/Bangui"
  },
  {
    "timezone_id": 8,
    "timezone_name": "Africa/Banjul"
  },
  {
    "timezone_id": 9,
    "timezone_name": "Africa/Bissau"
  },
  ......
]
```

Every timezone has a `timezone_id` attached; this will be used when calling the Strela API for timezone manipulation.



### Timezone Queries

This endpoint converts the current UTC time to a timezone of your choice, specified by the `timezone_id` of the timezone. To call this endpoint, use `/timezones/convert?timezone_id=x` where `x` is the timezone_id.

If one was to find out the current time on Wake Island, for instance: `/timezones/convert?timezone_id=420`

Response:

```json
{
  "utc": "10-21-2016 10:40:20 -0000",
  "pacific/wake": "10-21-2016 22:40:20 +1200",
  "format": "MM-DD-YYYY HH:mm:SS Z"
}
```

The response object contains the current UTC time, the time in Wake Island(Pacific/Wake), as well as the format string used to marshal the converted timestamps into strings. Eventually, you would be able to specify your own format strings while calling the API.