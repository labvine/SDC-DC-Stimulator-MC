# SDC-DC-Stimulator-MC
Signal Data Creators for DC-Stimulator MC equipment (neuroConn, GmbH). This repository contains a set of Python scripts for creating various custom data signals in a form of MATLAB data files (\*.mat), which can be next converted with the use of neuroConn-BinaryFileSignal-Creator software (neuroConn, GmbH) into BinaryFileSignal format (\*.bfs). BFS files can be next transferred to the panel-pc of the DC-Stimulator MC equipment and then used as a current stimulation signal.

**Creation of the input \*.mat files**

A MATLAB file that is suitable for the conversion into \*.bfs file has to contain the variables `data` (data vector) and `fs` (sample rate). The data vector contains the signal values in μA. The sample rate is given in samples per second (smp/sec). The DC-Stimulator MC generates signals with a sample rate of 16000 smp/sec per default. Unless otherwise specified, you must use this sample rate. To create a suitable input \*.mat file in Python you can start with (see also <a href="https://github.com/labvine/SDC-DC-Stimulator-MC/blob/master/Default.py">Default.py</a> script):

```python
import numpy as np
import scipy.io as sio

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
```

In order to create an arbitrary data signals consisted of repetitive pulses based on different waveforms, you can consider using `custom_alternating_signal` function from <a href="https://github.com/labvine/SDC-DC-Stimulator-MC/blob/master/AlternatingSignals/CustomAlternatingSignal.py">CustomAlternatingSignal.py</a> script. Below is one example of using this function, as well as image of resulting data signal.

```python
import AlternatingSignals.CustomAlternatingSignal as cas

# Define parameters.
samp_rate = 16000
stim_shape = "sinusoidal"
first_peak_pol = "positive"
freq = 1.0
amp = 1000
off_amp = 0
sig_dur = 10.0
pulse_dur = 0.5
pre_post_dur = [1.0, 1.0]
save_mat = (False, "Signal.mat")
preview_sig = True

# Call function.
data_signal = cas.custom_alternating_signal(samp_rate=samp_rate, stim_shape=stim_shape, first_peak_pol=first_peak_pol,
                                            freq=freq, amp=amp, off_amp=off_amp, sig_dur=sig_dur, pulse_dur=pulse_dur,
                                            pre_post_dur=pre_post_dur, save_mat=save_mat, preview_sig=preview_sig)
```

Preview of the `data_signal` vector:

<img src="https://github.com/labvine/SDC-DC-Stimulator-MC/blob/master/AlternatingSignals/Fig1.png" width="60%">

Author: Piotr Dzwiniel

Contact: piotr.dzwiniel@gmail.com
