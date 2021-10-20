import json
import requests

while True:
    result = requests.get('http://api.open-notify.org/iss-now.json').json()
    lat = result['iss_position']['latitude']
    long = result['iss_position']['longitude']

    print(lat, long)
    data = {'lat': lat, 'long': long}
    json_data = json.dumps(data)
    with open('data.json', 'w') as out:
        out.write(json_data)
