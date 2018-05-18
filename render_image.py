#!/usr/bin/env python3

"""
    render_image.py - python3 program to render matplotlib images
    Created: Sadip Giri (sadipgiri@bennington.edu)
    Date: 17th May, 2018
"""

import matplotlib.pyplot as plt
from sensor_api import dict_of_sensors_list, last_hour_sensor_data

def render_img(data):
    temps = data["temps"]
    humids = data["humids"]
    # timestamps = data["timestamps"]
    plt.plot(temps, humids)
    plt.xlabel("Temperature in Celcius")
    plt.ylabel("Humidity in %")
    plt.savefig('{0}pic.png'.format('./static/'))

if __name__ == '__main__':
    print(last_hour_sensor_data())
    data = dict_of_sensors_list(last_hour_sensor_data())
    render_img(data)



