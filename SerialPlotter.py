# Code for serial plotter

# ----- MODULES ----------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
import sys
import serial
import serial.tools.list_ports
import time

# --------- SERIALPLOTTER CLASS ---------------------------------

class SerialPlotter: 

    def __init__(self, ax, twidth):                                     # ax - axis object where line will be plotted, twidth - length of time window for x axis, dt - time incr. between data points
       
        self.ax = ax
        self.twidth = twidth

        self.tdata = [0] # to hold time values
        self.ydata = [0] # to hold sensor values

        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim()      # add y limits
        self.ax.set_xlim(0, twidth)      # add x limits 

    def update(self, y, t):            # method to add a y-value to the plot and update it 

        self.tdata.append(t)
        self.ydata.append(y)
        self.line.set_data(self.tdata, self.ydata)
        return self.line,


# -------- SELECTING AND OPENING SERIAL PORT ------------------------------------------------

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
port = ''
portList = []

print("\n List of available ports \n")
for onePort in ports:
    portList.append(str(onePort.device))
    print(str(onePort))

port = input("\n select port \n")

if port not in portList:
    print("Invalid port chosen")
    sys.exit(1)

print("\n Port selected: ")
print(port)

# OPEN PORT

#get baud rate from user
chosenBaud = input("\n select baud rate \n")
serialInst.baudrate = chosenBaud

serialInst.port = port
serialInst.open()
print("\n port open \n")

# -------- MAIN ------------------------------------------------

fig, ax = plt.subplots()
plotter = SerialPlotter(ax,10)

start_time = time.time()

while True:

    if serialInst.in_waiting:

        current_time = time.time()
        time_elapsed = current_time - start_time        # get t values for x axis

        data_raw = serialInst.readline()
        data_strip=data_raw.decode('utf-8').rstrip()
        sensor_reading = float(data_strip)    # get sensor reading for y axis 

        plotter.update(sensor_reading, time_elapsed)
        plt.pause(0.01)

        
        