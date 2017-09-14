# SDC-DC-Stimulator-MC
Signal Data Creators for DC-Stimulator MC equipment (neuroConn, GmbH). This repository contains a set of Python scripts for creating various custom data signals in a form of MATLAB data files (\*.mat), which can be next converted with the use of neuroConn-BinaryFileSignal-Creator software (neuroConn, GmbH) into BinaryFileSignal format (\*.bfs). BFS files can be next transferred to the panel-pc of the DC-Stimulator MC equipment and then used as a current stimulation signal.

**Creation of the input \*.mat files**
A MATLAB file that is suitable for the conversion into \*.bfs file has to contain the variables `data` (data vector) and `fs` (sample rate). The data vector contains the signal values in μA. The sample rate is given in samples per second (smp/sec). The DC-Stimulator MC generates signals with a sample rate of 16000 smp/sec per default. Unless otherwise specified, you must use this sample rate. To create a suitable input \*.mat file in Python you can start with:

```python
import numpy as np
import scipy.io as sci

# Determination of the sample rate.
fs = 16000

# Determination of the signal length in seconds.
numSec = 10

# Creation of a time vector.
t = np.arange(0, numSec - 1 / fs, 1 / fs)

# Magnitude in μA.
amp = 1000

# Frequency in Hz.
freq = 3

# Offset in μA.
off = 500

# Creation of a data vector.
data = np.sin(2 * np.pi * freq * t) * amp + off

# Saving in MAT-File format.
sci.savemat("Signal.mat", mdict={"data": data, "fs": fs})
```
