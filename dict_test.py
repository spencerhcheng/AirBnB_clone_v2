#!/usr/bin/python3
params = ['city_id="0001"', 'user_id="0001"', 'name="My_little_house"', 'number_rooms=4', 'number_bathrooms=2', 'max_guest=10', 'price_by_night=300', 'latitude=37.773972', 'longitude=-122.431297']

list_2 = []

for param in params:
    list_2.append(param.split("="))
print("here's the list: {} ".format(list_2))

for i in list_2:
    print(i)
