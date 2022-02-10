'''
Plot:
    The plot() function is used to draw points (markers) in a diagram.
    By default, the plot() function draws a line from point to point.
'''
#The x-axis is the horizontal axis.
#The y-axis is the vertical axis.

import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])
# plt.plot(xpoints, ypoints)
# plt.show()

'''
Plotting Without Line:
    To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.
'''
# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])
# plt.plot(xpoints, ypoints, 'o')
# plt.show()

#Multiple Points:
    #For multiple Points make sure you have the same number of points in both axis.
# xpoints = np.array([1, 2, 6, 8])
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(xpoints, ypoints)
# plt.show()

'''
Default X-Points:
    If we do not specify the points in the x-axis, they will get the default values 0, 1, 2, 3, (etc. depending on the length of the y-points)
'''
# ypoints = np.array([3, 8, 1, 10, 5, 7])
# plt.plot(ypoints)
# plt.show()

















