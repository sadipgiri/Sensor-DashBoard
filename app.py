#!/usr/bin/env python3

from flask import Flask, render_template
from sensor_api import dict_of_sensors_list, last_hour_sensor_data
# from render_image import render_img

app = Flask(__name__)

@app.route('/')
def index():
    data = last_hour_sensor_data()
    # data = dict_of_sensors_list(data)
    print(data)
    # fig = render_img(data)
    # return render_template('home.html', data=data)
    list_of_sensors = list(range(1, 21))
    # list_of_sensors = ["1", "2"]
    return render_template('sensor.html', data=data, list_of_sensors=list_of_sensors)

@app.route('/id')
def 

if __name__ == '__main__':
    app.run(debug=True)
