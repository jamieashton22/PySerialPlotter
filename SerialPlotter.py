# Code for serial plotter

# ----- MODULES ----------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from matplotlib.lines import Line2D


# --------- SERIALPLOTTER CLASS ---------------------------------

class SerialPlotter: 
    def __init__(self, ax, twidth, dt):                                     # ax - axis object where line will be plotted, twidth - length of time window for x axis, dt - time incr. between data points
       
        self.ax = ax
        self.twidth = twidth
        self.dt = dt

        self.tdata = [0] # to hold time values
        self.ydata = [0] # to hold sensor values

        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim()      # add y limits
        self.ax.set_xlim(0, twidth)      # add x limits 

    def update(self, y):            # method to add a y-value to the plot and update it 
        t = self.tdata[-1] + self.dt

        self.tdata.append(t)
        self.ydata.append(y)
        self.line.set_data(self.tdata, self.ydata)
        return self.line,



# -------- MAIN ------------------------------------------------

