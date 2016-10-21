## Strela

This doc outlines the main endpoints exposed by the Strela API, as well as what kind of parameters they accept and the responses they return.



### All Timezones

This endpoint returns a list of all timezones that both Strela and the Arrow package support. The URL for this endpoint is `/timezones`. The response is like this:

```json
erguelen'}, {u'timezone_id': 378, u'timezone_name': u'Indian/Mahe'}, {u'timezone_id': 379, u'timezone_name': u'Indian/Maldives'}, {u
'timezone_id': 380, u'timezone_name': u'Indian/Mauritius'}, {u'timezone_id': 381, u'timezone_name': u'Indian/Mayotte'}, {u'timezone_
id': 382, u'timezone_name': u'Indian/Reunion'}, {u'timezone_id': 383, u'timezone_name': u'Pacific/Apia'}, {u'timezone_id': 384, u'ti
mezone_name': u'Pacific/Auckland'}, {u'timezone_id': 385, u'timezone_name': u'Pacific/Bougainville'}, {u'timezone_id': 386, u'timezo
ne_name': u'Pacific/Chatham'}, {u'timezone_id': 387, u'timezone_name': u'Pacific/Chuuk'}, {u'timezone_id': 388, u'timezone_name': u'
Pacific/Easter'}, {u'timezone_id': 389, u'timezone_name': u'Pacific/Efate'}, {u'timezone_id': 390, u'timezone_name': u'Pacific/Ender
bury'}, {u'timezone_id': 391, u'timezone_name': u'Pacific/Fakaofo'}, {u'timezone_id': 392, u'timezone_name': u'Pacific/Fiji'}, {u'ti
mezone_id': 393, u'timezone_name': u'Pacific/Funafuti'}, {u'timezone_id': 394, u'timezone_name': u'Pacific/Galapagos'}, {u'timezone_
id': 395, u'timezone_name': u'Pacific/Gambier'}, {u'timezone_id': 396, u'timezone_name': u'Pacific/Guadalcanal'}, {u'timezone_id': 3
97, u'timezone_name': u'Pacific/Guam'}, {u'timezone_id': 398, u'timezone_name': u'Pacific/Honolulu'}, {u'timezone_id': 399, u'timezo
ne_name': u'Pacific/Johnston'}, {u'timezone_id': 400, u'timezone_name': u'Pacific/Kiritimati'}, {u'timezone_id': 401, u'timezone_nam
e': u'Pacific/Kosrae'}, {u'timezone_id': 402, u'timezone_name': u'Pacific/Kwajalein'}, {u'timezone_id': 403, u'timezone_name': u'Pac
ific/Majuro'}, {u'timezone_id': 404, u'timezone_name': u'Pacific/Marquesas'}, {u'timezone_id': 405, u'timezone_name': u'Pacific/Midw
ay'}, {u'timezone_id': 406, u'timezone_name': u'Pacific/Nauru'}, {u'timezone_id': 407, u'timezone_name': u'Pacific/Niue'}, {u'timezo
ne_id': 408, u'timezone_name': u'Pacific/Norfolk'}, {u'timezone_id': 409, u'timezone_name': u'Pacific/Noumea'}, {u'timezone_id': 410
, u'timezone_name': u'Pacific/Pago_Pago'}, {u'timezone_id': 411, u'timezone_name': u'Pacific/Palau'}, {u'timezone_id': 412, u'timezo
ne_name': u'Pacific/Pitcairn'}, {u'timezone_id': 413, u'timezone_name': u'Pacific/Pohnpei'}, {u'timezone_id': 414, u'timezone_name':
 u'Pacific/Port_Moresby'}, {u'timezone_id': 415, u'timezone_name': u'Pacific/Rarotonga'}, {u'timezone_id': 416, u'timezone_name': u'
Pacific/Saipan'}, {u'timezone_id': 417, u'timezone_name': u'Pacific/Tahiti'}, {u'timezone_id': 418, u'timezone_name': u'Pacific/Tara
wa'}, {u'timezone_id': 419, u'timezone_name': u'Pacific/Tongatapu'}, {u'timezone_id': 420, u'timezone_name': u'Pacific/Wake'}, {u'ti
mezone_id': 421, u'timezone_name': u'Pacific/Wallis'}]
```

Every timezone has a `timezone_id` attached; this will be used when calling the Strela API for timezone manipulation.



### Timezone Queries

This endpoint converts the current UTC time to a timezone of your choice, specified by the `timezone_id` of the timezone. To call this endpoint, use `/timezones/convert?timezone_id=x` where `x` is the timezone_id.

If one was to find out the current time on Wake Island, for instance: `/timezones/convert?timezone_id=420`

Response:

```json
{u'pacific/wake': u'10-21-2016 22:29:95 +1200', u'utc': u'10-21-2016 10:29:95 -0000', u'format': u'MM-DD-YYYY HH:mm:SS Z'} 
```

The response object contains the current UTC time, the time in Wake Island(Pacific/Wake), as well as the format string used to marshal the converted timestamps into strings. Eventually, you would be able to specify your own format strings while calling the API.