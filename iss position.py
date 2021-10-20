import requests

while True:
    result = requests.get('http://api.open-notify.org/iss-now.json').json()
    lat = result['iss_position']['latitude']
    long = result['iss_position']['longitude']
    print(lat, long)
