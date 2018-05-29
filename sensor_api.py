#!/usr/bin/env python3

"""
    sensor_api - python3 program to return sensor readings hitting the given endpoints
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Created: 15 May, 2018
"""
import re
import requests
import json

def last_hour_sensor_data():
    try:
        req = requests.request('GET', 'http://54.197.182.144:5000/read/last_hour')
        json_data = req.json()
        return json_data
    except Exception as e:
        return offline_sensor_data() 

def particular_sensor_data(id=1):
    if id:
        try:
            req = requests.request('GET', 'http://54.197.182.144:5000/read/{0}'.format(id))
            json_data = req.json()
            return json_data["data"]
        except Exception as e:
            return offline_sensor_data()
    try:
        req = requests.request('GET', 'http://34.201.69.120:5000/read/1')
        json_data = req.json()
        return json_data["data"]
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

def scan_sensors():
    dct = {}
    req = requests.request('GET', 'http://54.197.182.144:5000/scan')
    json_data = req.json()
    data = json_data["sensors"]
    for i in data:
        dct[i['id']] = i['location']
    return dct

def split_location(location):
    location = location.lower()
    match = re.match(r"([a-z]+)([0-9]+)", location, re.I)
    items = match.groups()
    return items

def convert():
    sensors = scan_sensors()
    x = []
    y = []
    temp = []
    id = []
    req = requests.request('GET', 'http://54.197.182.144:5000/read/last_hour')
    json_data = req.json()
    for i in json_data:
        if i["id"] not in id: 
            id.append(i["id"])
            loc_info = split_location(sensors[int(i["id"])])
            y.append(loc_info[0])
            x.append(loc_info[1])
            temp.append(i["data"]["temperature"]["value"])
    return {'y': y, 'x': x, 'temp': temp}


if __name__ == '__main__':
    # print(dict_of_sensors_list(last_hour_sensor_data()))
    # print(particular_sensor_data(id=5))
    print(scan_sensors())
    print(convert())
       

