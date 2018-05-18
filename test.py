#!/usr/bin/env python3
import matplotlib.pyplot as plt

plt.plot([0, 1, 2, 3, 4], [0, 3, 5, 9, 11])

plt.xlabel('X')
plt.ylabel('Y')
# plt.show()
plt.savefig('{0}pic.png'.format('./static/'))