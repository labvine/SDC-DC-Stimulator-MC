# Created by pdzwiniel at 2017-09-14.
# Contact: piotr.dzwiniel@gmail.com.
# This file is a part of SDC-DC-Stimulator-MC project.

import numpy as np
import scipy.io as sio

"""
Script for the creation of basic sinusoidal data signal
for alternating current stimulation.
"""

# Determination of the sample rate.
fs = 16000

# Determination of the signal length in seconds.
num_sec = 10

# Creation of a time vector.
t = np.arange(0, num_sec - 1 / fs, 1 / fs)

# Magnitude in μA.
amp = 1000

# Frequency in Hz.
freq = 3

# Offset in μA.
off = 500

# Creation of a data vector.
data = np.sin(2 * np.pi * freq * t) * amp + off

# Saving in MAT-File format.
sio.savemat("Signal.mat", mdict={"data": data, "fs": fs})
