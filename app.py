#!/usr/bin/env python3

"""
    app.py - Flask Application for Sensor Readings and Visualization
    Created: Sadip Giri (sadipgiri@bennington.edu)
    Date: 15th May, 2018
"""

from flask import Flask, render_template, request
from sensor_api import dict_of_sensors_list, last_hour_sensor_data, particular_sensor_data 
import time
from render_image import render_img, render_in_plotly, heat_map

app = Flask(__name__)

@app.route('/')
def index():
    # data_to_plot = dict_of_sensors_list(last_hour_sensor_data())
    # # render_img(data_to_plot)
    # # time.sleep(0.75)
    # render_in_plotly(data_to_plot)
    data = last_hour_sensor_data()
    # data = dict_of_sensors_list(data)
    list_of_sensors = list(range(1, 21))
    heat_map()  # to render the heat map before rendering the sensor_dashboard
    return render_template('sensor.html', data=data, list_of_sensors=list_of_sensors)

@app.route('/id', methods=['GET', 'POST'])
def id():
    select = request.form.get('IDs')
    print(select)
    # render_img(dict_of_sensors_list(particular_sensor_data(id=select)), select)
    render_in_plotly(dict_of_sensors_list(particular_sensor_data(id=select)), select)
    data = last_hour_sensor_data()
    list_of_sensors = list(range(1, 21))
    return render_template('sensor.html', data=data, list_of_sensors=list_of_sensors)
 

if __name__ == '__main__':
    app.run(debug=True)
