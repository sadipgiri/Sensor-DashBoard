#!/usr/bin/env python3

"""
    sensor_api - python3 program to return sensor readings hitting the given endpoints
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Created: 15 May, 2018
"""
import requests
import json

def last_hour_sensor_data():
    try:
        req = requests.request('GET', 'http://34.201.69.120:5000/read/last_hour')
        json_data = req.json()
        return json_data
    except Exception as e:
        return offline_sensor_data() 

def offline_sensor_data():
        with open('./offline_data/sensor_readings.json') as json_file:
                json_data = json.load(json_file)
        sensor_readings = json_data
        return sensor_readings

def dict_of_sensors_list(data):
    temps = []
    humids = []
    timestamps = []
    for i in data:
        temps.append(i["data"]["temperature"]["value"])
        humids.append(i["data"]["humidity"]["value"])
        timestamps.append(i["timestamp"])
    dicts = {"temps": temps, "humids": humids, "timestamps": timestamps}
    return dicts


if __name__ == '__main__':
    print(dict_of_sensors_list(last_hour_sensor_data()))
       

