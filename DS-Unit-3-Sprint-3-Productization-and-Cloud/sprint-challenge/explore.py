import openaq

api = openaq.OpenAQ()
status, body = api.measurements(city='Los Angeles', parameter='pm25')

body['results'][0]['date']['utc']
body['results'][0]['value']

Vals = []
for i in range(len(body['results'])):
    tim = body['results'][i]['date']['utc']
    val = body['results'][i]['value']
    tup = (tim, val)
    Vals.append(tup)

Vals
