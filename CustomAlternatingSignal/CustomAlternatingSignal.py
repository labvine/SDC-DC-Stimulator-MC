# Created by pdzwiniel at 2017-09-14.
# Contact: piotr.dzwiniel@gmail.com.
# This file is a part of SDC-DC-Stimulator-MC project.

"""
Script for creating an arbitrary data signals consisted of repetitive pulses based on three different waveform shapes,
ie. square, sawtooth and sinusoidal. You can specify signal duration, number of pulses in signal, duration of single
pulses, their amplitude, signal offset amplitude, as well as pre and post time duration, when non pulse occur.
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio

from CustomAlternatingSignal import OnePeriodSignals as ops


def custom_alternating_signal(samp_rate=16000, stim_shape="sinusoidal", first_peak_pol="positive", freq=0.1, amp=1000,
                              off_amp=0, sig_dur=10.0, pulse_dur=0.1, pre_post_dur=[1.0, 1.0],
                              save_mat=(False, "Signal.mat"), preview_sig=False):
    """
    Function for creating an arbitrary data signals consisted of repetitive pulses based on three different waveform
    shapes, ie. square, sawtooth and sinusoidal. The whole list of parameters one can specify is provided below.
    Check also the examples section for more detailed information about use of this function.

    Parameters
    ----------
    samp_rate : int
        Sampling rate of the data signal. Default value is set to 16000 in accordance to requirements
        of DC-Stimulator MC equipment (neuroConn, GmbH).
    stim_shape : ["square", "sawtooth", "sinusoidal"]
        Shape of the stimulation pulses. Data signal consists of one-period waveforms (pulses) of one of the three
        available shapes. Default value is "sinusoidal".
    first_peak_pol : ["positive", "negative"]
        Stimulation pulse can start with positive or negative wave. Default value is "positive".
    freq : float
        Number of stimulation pulses per second, in other words - frequency in Hz. Frequency value has to meet
        the following assumption: "sig_dur < (1.0 / freq)". Otherwise, ValueError will rise. Default value
        is 10.0.
    amp : int
        Stimulation pulse amplitude in μA. Default value is 1000.
    off_amp : int
        Offset amplitude of the data signal. Default value is 0.
    sig_dur : float
        Data signal duration in seconds. Default value is 10.0.
    pulse_dur : float
        Single stimulation pulse duration in seconds. Pulse duration has to meet the following assumption:
        "pulse_dur > (1.0 / freq)". Otherwise, ValueError will rise. Default value is 0.5.
    pre_post_dur : [float, float]
        Pre and post offset time in seconds added to the data signal. Default values are [1.0, 1.0].
    save_mat : (boolean, String)
        Tuple consisted of two values. First boolean value decide whether data signal will be saved as a MATLAB-File
        (*.mat) with two variables in mdictionary, ie. "data" (data signal) and "fs" (sampling rate). Second String
        value define name for the aforementioned file. Default values are (False, "Signal.mat").
    preview_sig : boolean
        If True, preview of the data signal will be shown with the use of matplotlib.pyplot library. Default value
        is False.

    Returns
    -------
    data_signal : ndarray
        One-dimensional data signal.

    Examples
    --------
    Make sure, that scripts "OnePeriodSignals.py" and "CustomAlternatingSignal.py" are in the same folder. Than,
    you can use this function as follows.

    Example 1 :
    from CustomAlternatingSignal import CustomAlternatingSignal as cas

    data_signal = cas.custom_alternating_signal()

    Example 2 :
    from CustomAlternatingSignal import CustomAlternatingSignal as cas

    # Define parameters.
    samp_rate = 16000
    stim_shape = "sinusoidal"
    first_peak_pol = "positive"
    freq = 0.1
    amp = 1000
    off_amp = 0
    sig_dur = 10.0
    pulse_dur = 0.1
    pre_post_dur = [1.0, 1.0]
    save_mat = (False, "Signal.mat")
    preview_sig = True

    # Call function.
    data_signal = cas.custom_alternating_signal(samp_rate=samp_rate, stim_shape=stim_shape, first_peak_pol=first_peak_pol,
                                                freq=freq, amp=amp, off_amp=off_amp, sig_dur=sig_dur, pulse_dur=pulse_dur,
                                                pre_post_dur=pre_post_dur, save_mat=save_mat, preview_sig=preview_sig)
    """

    # Check assumption for frequency parameter.
    if sig_dur < (1.0 / freq):
        f = ("%f" % (1.0 / sig_dur)).rstrip('0').rstrip('.')
        error_text = "Stimulation frequency (freq) is to high in accordance to stimulation signal length (sig_dur). " \
                     "In current conditions it should not exceed " + f + "."
        raise ValueError(error_text)

    # Check assumption for pulse duration parameter.
    if pulse_dur > (1.0 / freq):
        f = ("%f" % (1.0 / freq)).rstrip('0').rstrip('.')
        raise ValueError("Pulse duration (pd) value can't be higher than " + f + ".")

    # Prepare pre and post offset time vectors.
    pre = [0] * int(samp_rate * pre_post_dur[0])
    post = [0] * int(samp_rate * pre_post_dur[1])

    # Creation of a data signal vector.
    data_signal = []

    # Calculate total number of pulses in signal.
    tot = sig_dur * freq

    # Populate data signal vector in accordance to stimulus shape parameter.
    if stim_shape == "square":

        # Create trials with pulses and add them to vector data.
        i = 0
        while i < tot:
            trial = np.zeros(samp_rate * sig_dur / tot)
            trial[0:pulse_dur * samp_rate] = ops.square_pulse(samp_rate, pulse_dur, amp, first_peak_polarity=first_peak_pol)
            data_signal.extend(trial)
            i += 1
        data_signal = pre + data_signal + post

    elif stim_shape == "sawtooth":

        # Create trials with pulses and add them to vector data.
        i = 0
        while i < tot:
            trial = np.zeros(samp_rate * sig_dur / tot)
            trial[0:pulse_dur * samp_rate] = ops.sawtooth_pulse(samp_rate, pulse_dur, amp, first_peak_polarity=first_peak_pol)
            data_signal.extend(trial)
            i += 1
        data_signal = pre + data_signal + post

    elif stim_shape == "sinusoidal":

        # Create trials with pulses and add them to vector data.
        i = 0
        while i < tot:
            trial = np.zeros(samp_rate * sig_dur / tot)
            trial[0:pulse_dur * samp_rate] = ops.sin_pulse(samp_rate, pulse_dur, amp, first_peak_polarity=first_peak_pol)
            data_signal.extend(trial)
            i += 1
        data_signal = pre + data_signal + post

    else:
        raise ValueError("Invalid stimulation pulse shape (stim_shape)")

    # Convert data type (list) to ndarray and add offset.
    data_signal = np.asarray(data_signal) + off_amp

    # Saving in MATLAB-File format.
    if save_mat[0]:
        sio.savemat(save_mat[1], mdict={"data": data_signal, "fs": samp_rate})

    # Preview created data signal.
    if preview_sig:
        plt.plot(data_signal)
        plt.show()

    # Return data signal.
    return data_signal
