#!/usr/bin/env python3

"""
    render_image.py - python3 program to render matplotlib images
    Created: Sadip Giri (sadipgiri@bennington.edu)
    Date: 17th May, 2018
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import plotly.offline as offline
import plotly.graph_objs as go

from sensor_api import dict_of_sensors_list, last_hour_sensor_data, convert

def render_img(data):
    temps = data["temps"]
    humids = data["humids"]
    timestamps = data["timestamps"]
    # plt.plot(temps, humids)
    plt.plot(timestamps, temps)
    # plt.xlabel("Temperature in Celcius")
    # plt.title("Its Pi with {0} ID".format(id))
    plt.title("last Hour Temperature Data")
    plt.xlabel("Timestamp")
    plt.ylabel("Temperature in C")
    plt.savefig('{0}pic.png'.format('./static/'))

def render_in_plotly(data, id):
    # remove_html()
    trace1 = go.Scatter(x=data["timestamps"], y=data["temps"])
    trace2 = go.Scatter(x=data["timestamps"], y=data["humids"])
    layout = go.Layout(title='{0} Plot'.format(id), plot_bgcolor='rgb(230,230,230)')
    fig = go.Figure(data=[trace1, trace2], layout=layout)
    offline.plot(fig, filename='{0}simple.html'.format('./static/'), auto_open=False)
    return

# need to pass that last hour data and it will work!
def heat_map(data):
    # raw_data = pd.read_csv('./static/file.csv')
    raw_data = pd.DataFrame({'x':data['x'], 'y':data['y'], 'temp': data['temp']})
    raw_data["y"] = pd.Categorical(raw_data["y"], raw_data.y.unique())
    print("y: {0}".format(raw_data["y"]))
    print("x: {0}".format(raw_data["x"]))
    print(raw_data)
    print("  ")
    raw_data.head()
    temp_matrix = raw_data.pivot(index="y", columns="x", values="temp")
    fig = plt.figure()
    fig, ax = plt.subplots(1,1, figsize=(12,8))
    heatplot = ax.imshow(temp_matrix, cmap='BuPu')
    ax.set_xticklabels(temp_matrix.columns)
    ax.set_yticklabels(temp_matrix.index)
    tick_spacing = 1
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax.set_title("Heatmap of test room")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.savefig('{0}heat_map.png'.format('./static/'), dpi=100)

# def remove_html():
#     html_file = "./static/simple.html"
#     if os.path.isfile(html_file):
#         os.remove(html_file)
#     else:
#         print("Error: %s file doesnot exist" % simple.html)


if __name__ == '__main__':
    # print(last_hour_sensor_data())
    data1 = dict_of_sensors_list(last_hour_sensor_data())
    render_img(data1)
    # data_to_plot = dict_of_sensors_list(last_hour_sensor_data())
    # render_in_plotly(data_to_plot, 1)
    # remove_html()
    # heat_map()
    data = convert()
    heat_map(data)

