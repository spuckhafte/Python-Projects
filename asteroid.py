import requests
import datetime
import time

year = datetime.datetime.today().year
month = datetime.datetime.today().month
day = datetime.datetime.today().day

print(f'\nToday: {day}-{month}-{year}')
print('Information of Potentially Hazardous NEOs')
time.sleep(0.5)
print('\nfetching...')

result = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?start_date={year}-{month}-{day}&end_date={year}-{month}-{day}&api_key=ZOU1Yv9ghEmsvehJtlQV12TyuFhdUylm02bh08Ge')
result = result.json()

info = result['near_earth_objects'][f'{year}-{month}-{day}']

names = []
diameters = []
closest_approach_date = []
relative_velocity = []
miss = []
hazardous = []

for asteroid in info:
    min_dia = asteroid['estimated_diameter']['meters']['estimated_diameter_min']
    max_dia = asteroid['estimated_diameter']['meters']['estimated_diameter_max']
    diameters.append([min_dia, max_dia])

for asteroid in info:
    relative_velocity.append(asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_second'])

for asteroid in info:
    miss.append(asteroid['close_approach_data'][0]['miss_distance']['kilometers'])

for asteroid in info:
    names.append(asteroid['name'])

for asteroid in info:
    closest_approach_date.append(asteroid['close_approach_data'][0]['close_approach_date_full'])

i = 0
while i < len(info):
    if info[i]['is_potentially_hazardous_asteroid']:
        hazardous.append(i)
    i += 1

i = 0
while i < len(names):
    if i in hazardous:
        print(f'''
        Near Earth Object: {names[i]}
        Minimum Diameter: {diameters[i][0]} m
        Maximum Diameter: {diameters[i][1]} m
        Closest Approach Date: {closest_approach_date[i]}
        Relative Velocity: {relative_velocity[i]} km/s
        Miss Distance: {miss[i]} km
        ''')
    i += 1

time.sleep(1)

print('-------------------------------------------\nInformation of all NEOs')
time.sleep(0.5)
print('\nfetching...')
time.sleep(3)

i = 0
while i < len(names):
    print(f'''
    Near Earth Object: {names[i]}
    Minimum Diameter: {diameters[i][0]} m
    Maximum Diameter: {diameters[i][1]} m
    Closest Approach Date: {closest_approach_date[i]}
    Relative Velocity: {relative_velocity[i]} km/s
    Miss Distance: {miss[i]} km
    ''')
    i += 1
    time.sleep((0.5))
