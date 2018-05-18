#!/usr/bin/env python3

"""
    app.py - Flask Application for Sensor Readings and Visualization
    Created: Sadip Giri (sadipgiri@bennington.edu)
    Date: 15th May, 2018
"""

from flask import Flask, render_template
from sensor_api import dict_of_sensors_list, last_hour_sensor_data
import time
from render_image import render_img

app = Flask(__name__)

@app.route('/')
def index():
    data_to_plot = dict_of_sensors_list(last_hour_sensor_data())
    render_img(data_to_plot)
    # time.sleep(0.75)
    data = last_hour_sensor_data()
    # data = dict_of_sensors_list(data)
    print(data)
    list_of_sensors = list(range(1, 21))
    return render_template('sensor.html', data=data, list_of_sensors=list_of_sensors)

# @app.route('/id')
# def 

if __name__ == '__main__':
    app.run(debug=True)
