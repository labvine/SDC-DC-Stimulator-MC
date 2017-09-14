# Created by pdzwiniel at 2017-09-14.
# Contact: piotr.dzwiniel@gmail.com.
# This file is a part of SDC-DC-Stimulator-MC project.

"""
Script for creating arbitrary data signals consisted of repetitive pulses based on three different waveform shapes,
ie. square, sawtooth and sinusoidal. You can specify signal duration, number of pulses in signal, duration of single
pulses, their amplitude, signal offset amplitude, as well as pre and post time duration, when non pulse occur.

TODO: Enclose script functionality in one function.
TODO: Enclose script and its project dependencies in one dedicated folder.
"""

import numpy as np
import OnePeriodSignals as ops
import scipy.io as sio
import matplotlib.pyplot as plt

# Determination of the sample rate.
sr = 16000  # 16000 sample rate is required for DC-Stimulator MC *.bfs format.

# Determination of stimulation pulse shape.
stim_shape = ["square", "sawtooth", "sinusoidal"][2]

# Determination of first peak polarity of the stimulation pulse.
first_peak_polarity = ["positive", "negative"][0]

# Determination of the stimulation signal length in seconds.
sig_dur = 10.0

# Stimulation frequency in Hz (pulses per second).
freq = 1.0
if sig_dur < (1.0 / freq):
    f = ("%f" % (1.0 / sig_dur)).rstrip('0').rstrip('.')
    error_text = "Stimulation frequency (freq) is to high in accordance to stimulation signal length (sig_dur). " \
                 "In current conditions it should not exceed " + f + "."
    raise ValueError(error_text)

# Stimulation pulse duration in seconds (can't be lower than 1 / freq).
pd = 0.5
if pd > (1.0 / freq):
    f = ("%f" % (1.0 / freq)).rstrip('0').rstrip('.')
    raise ValueError("Pulse duration (pd) value can't be higher than " + f + ".")

# Stimulation pulse amplitude in μA.
amp = 1000

# Stimulation offset in μA.
off = 0

# Add pre and post offset time in seconds to the stimulation signal.
pre_post = [1.0, 1.0]
pre = [0] * int(sr * pre_post[0])
post = [0] * int(sr * pre_post[1])

# Creation of a data vector.
data = []

# Calculate total number of pulses in signal.
tot = sig_dur * freq

if stim_shape == "square":

    # Create trials with pulses and add them to vector data.
    i = 0
    while i < tot:
        trial = np.zeros(sr * sig_dur / tot)
        trial[0:pd * sr] = ops.square_pulse(sr, pd, amp, first_peak_polarity=first_peak_polarity)
        data.extend(trial)
        i += 1
    data = pre + data + post

elif stim_shape == "sawtooth":

    # Create trials with pulses and add them to vector data.
    i = 0
    while i < tot:
        trial = np.zeros(sr * sig_dur / tot)
        trial[0:pd * sr] = ops.sawtooth_pulse(sr, pd, amp, first_peak_polarity=first_peak_polarity)
        data.extend(trial)
        i += 1
    data = pre + data + post

elif stim_shape == "sinusoidal":

    # Create trials with pulses and add them to vector data.
    i = 0
    while i < tot:
        trial = np.zeros(sr * sig_dur / tot)
        trial[0:pd * sr] = ops.sin_pulse(sr, pd, amp, first_peak_polarity=first_peak_polarity)
        data.extend(trial)
        i += 1
    data = pre + data + post

else:
    raise ValueError("Invalid stimulation pulse shape (stim_shape)")

# Convert data type (list) to ndarray and add offset.
data = np.asarray(data) + off

# Saving in MAT-File format.
save_signal = True
if save_signal:
    sio.savemat("Signal.mat", mdict={"data": data, "fs": sr})

# Preview created signal.
preview_signal = False
if preview_signal:
    plt.plot(data)
    plt.show()
