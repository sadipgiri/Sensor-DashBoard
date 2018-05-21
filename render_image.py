#!/usr/bin/env python3

"""
    render_image.py - python3 program to render matplotlib images
    Created: Sadip Giri (sadipgiri@bennington.edu)
    Date: 17th May, 2018
"""

import matplotlib.pyplot as plt
from sensor_api import dict_of_sensors_list, last_hour_sensor_data
import plotly.offline as offline
import plotly.graph_objs as go
from sensor_api import dict_of_sensors_list, last_hour_sensor_data

def render_img(data):
    temps = data["temps"]
    humids = data["humids"]
    timestamps = data["timestamps"]
    # plt.plot(temps, humids)
    plt.plot(timestamps, humids)
    # plt.xlabel("Temperature in Celcius")
    plt.xlabel("Timestamp")
    plt.ylabel("Humidity in %")
    plt.savefig('{0}pic.png'.format('./static/'))

def render_in_plotly(data):
    trace1 = go.Scatter(x=data["timestamps"], y=data["temps"])
    trace2 = go.Scatter(x=data["timestamps"], y=data["humids"])
    layout = go.Layout(title='Sample Plot', plot_bgcolor='rgb(230,230,230)')
    fig = go.Figure(data=[trace1, trace2], layout=layout)
    offline.plot(fig, filename='{0}simple.html'.format('./static/'))

if __name__ == '__main__':
    # print(last_hour_sensor_data())
    # data = dict_of_sensors_list(last_hour_sensor_data())
    # render_img(data)
    data_to_plot = dict_of_sensors_list(last_hour_sensor_data())
    render_in_plotly(data_to_plot)


