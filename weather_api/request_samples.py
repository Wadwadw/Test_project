import json

import requests

cities_url = 'http://127.0.0.1:5000/cities'
cities = requests.get(cities_url)
cities_object = json.loads(cities.text)
cities_print = json.dumps(cities_object, indent=2)
print('These are examples of request output cities')
print('-----------------------------------------------------')
print('/cities')
print(cities_print)

print('-----------------------------------------------------')


mean_url_1 = 'http://127.0.0.1:5000/mean?value_type=temp&city=Dnipro'
mean_url_2 = 'http://127.0.0.1:5000/mean?value_type=clouds&city=Kharkiv'
mean_1 = requests.get(mean_url_1)
mean_2 = requests.get(mean_url_2)
mean_1_object = json.loads(mean_1.text)
mean_1_print = json.dumps(mean_1_object, indent=2)
print('These are examples of request output mean')
print('-----------------------------------------------------')
print('/mean?value_type=temp&city=Dnipro')
print(mean_1_print)
mean_2_object = json.loads(mean_2.text)
mean_2_print = json.dumps(mean_2_object, indent=2)
print('/mean?value_type=clouds&city=Kharkiv')
print(mean_2_print)

print('-----------------------------------------------------')

records_url_1 = 'http://127.0.0.1:5000/records?city=Kyiv&start_dt=2021-12-14&end_dt=2021-12-15'
records_url_2 = 'http://127.0.0.1:5000/records?city=Lviv&start_dt=2021-12-16&end_dt=2021-12-20'
records_1 = requests.get(records_url_1)
records_2 = requests.get(records_url_2)
records_1_object = json.loads(records_1.text)
records_1_print = json.dumps(records_1_object, indent=2)
print('These are examples of request output records')
print('-----------------------------------------------------')
print('/records?city=Kyiv&start_dt=2021-12-14&end_dt=2021-12-15')
print(records_1_print)
records_2_object = json.loads(records_2.text)
records_2_print = json.dumps(records_2_object, indent=2)
print('/records?city=Lviv&start_dt=2021-12-16&end_dt=2021-12-20')
print(records_2_print)

print('-----------------------------------------------------')

moving_mean_url_1 = 'http://127.0.0.1:5000/moving_mean?value_type=clouds&city=Kharkiv'
moving_mean_url_2 = 'http://127.0.0.1:5000/moving_mean?value_type=wind_speed&city=Ternopil'
moving_mean_1 = requests.get(moving_mean_url_1)
moving_mean_2 = requests.get(moving_mean_url_2)
moving_mean_1_object = json.loads(moving_mean_1.text)
moving_mean_1_print = json.dumps(moving_mean_1_object, indent=2)
print('These are examples of request output moving mean')
print('-----------------------------------------------------')
print('/moving_mean?value_type=clouds&city=Kharkiv')
print(moving_mean_1_print)
moving_mean_2_object = json.loads(moving_mean_2.text)
moving_mean_2_print = json.dumps(moving_mean_2_object, indent=2)
print('/moving_mean?value_type=wind_speed&city=Ternopil')
print(moving_mean_2_print)
