#! /usr/bin/env python3
"""
    heatmap_generator.py - Generates a heatmap image using provided data
    Author: nideshchitrakar
    Date: 05/19/18
"""

import pandas as pd

import matplotlib.ticker as ticker

import matplotlib.pyplot as plt


raw_data = pd.read_csv('dummy_data.csv')
raw_data["y"] = pd.Categorical(raw_data["y"], raw_data.y.unique())
raw_data.head()

temp_matrix = raw_data.pivot("y", "x", "temp")

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


plt.savefig('test.png', dpi=100)