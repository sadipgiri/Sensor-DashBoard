#!/usr/bin/env python3

import matplotlib.pyplot as plt
from sensor_api import dict_of_sensors_list

def render_img(data):
    temps = data["temps"]
    humids = data["humids"]
    plt.plot(temps, humids)
    return plt


if __name__ == '__main__':
    data = dict_of_sensors_list()
    render_img(data).show()



