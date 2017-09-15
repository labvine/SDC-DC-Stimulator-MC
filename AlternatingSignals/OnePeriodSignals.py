# Created by pdzwiniel at 2017-09-14.
# Contact: piotr.dzwiniel@gmail.com.
# This file is a part of SDC-DC-Stimulator-MC project.

import numpy as np
from scipy import signal as sig


def square_pulse(samp_rate, pulse_dur, amp, first_peak_pol="positive"):
    """
    Function for creating a specific one period squarewave pulse.

    Parameters
    ----------
    samp_rate : int
        Sampling rate of the pulse.
    pulse_dur : float
        Pulse duration in seconds.
    amp : int
        Pulse amplitude in μA.
    first_peak_pol : ["positive", "negative"]
        Polarity of the first pulse hillock. Default value is "positive".

    Returns
    -------
    pulse : ndarray
        Pulse in a form of one-dimmensional ndarray.
    """
    t = np.arange(0, pulse_dur, 1.0 / samp_rate)
    freq = 1.0 / pulse_dur
    pulse = sig.square(2 * np.pi * freq * t) * (amp / 2)
    if first_peak_pol == "positive":
        pass
    elif first_peak_pol == "negative":
        pulse *= -1
    else:
        raise ValueError("Invalid value of the first_peak_pol argument. Use \"positive\" or \"negative\".")
    return pulse


def sawtooth_pulse(samp_rate, pulse_dur, amp, first_peak_pol="positive"):
    """
    Function for creating a specific one period sawtooth pulse.

    Parameters
    ----------
    samp_rate : int
        Sampling rate of the pulse.
    pulse_dur : float
        Pulse duration in seconds.
    amp : int
        Pulse amplitude in μA.
    first_peak_pol : ["positive", "negative"]
        Polarity of the first pulse hillock. Default value is "positive".

    Returns
    -------
    pulse : ndarray
        Pulse in a form of one-dimmensional ndarray.
    """
    t = np.arange(0, pulse_dur, 1.0 / samp_rate)
    freq = 1.0 / pulse_dur
    pulse = sig.sawtooth(2 * np.pi * freq * t) * (amp / 2)
    if first_peak_pol == "positive":
        pass
    elif first_peak_pol == "negative":
        pulse *= -1
    else:
        raise ValueError("Invalid value of the first_peak_pol argument. Use \"positive\" or \"negative\".")
    return pulse


def sin_pulse(samp_rate, pulse_dur, amp, first_peak_pol="positive"):
    """
    Function for creating a specific one period sinusoidal pulse.

    Parameters
    ----------
    samp_rate : int
        Sampling rate of the pulse.
    pulse_dur : float
        Pulse duration in seconds.
    amp : int
        Pulse amplitude in μA.
    first_peak_pol : ["positive", "negative"]
        Polarity of the first pulse hillock. Default value is "positive".

    Returns
    -------
    pulse : ndarray
        Pulse in a form of one-dimmensional ndarray.
    """
    t = np.arange(0, pulse_dur, 1.0 / samp_rate)
    freq = 1.0 / pulse_dur
    pulse = np.sin(2 * np.pi * freq * t) * (amp / 2)
    if first_peak_pol == "positive":
        pass
    elif first_peak_pol == "negative":
        pulse *= -1
    else:
        raise ValueError("Invalid value of the first_peak_pol argument. Use \"positive\" or \"negative\".")
    return pulse
