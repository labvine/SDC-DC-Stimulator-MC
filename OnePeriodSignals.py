# Created by pdzwiniel at 2017-09-14.
# Contact: piotr.dzwiniel@gmail.com.
# This file is a part of SDC-DC-Stimulator-MC project.

import numpy as np
from scipy import signal as sig


def square_pulse(sr, dur, amp, first_peak_polarity="positive"):
    """
    :param sr: sampling rate
    :param dur: duration in seconds
    :param amp: amplitude in μA
    :param first_peak_polarity: "positive" or "negative"
    :return: square pulse
    """
    t = np.arange(0, dur, 1.0 / sr)
    freq = 1.0 / dur
    s = sig.square(2 * np.pi * freq * t) * (amp / 2)
    if first_peak_polarity == "positive":
        pass
    elif first_peak_polarity == "negative":
        s *= -1
    else:
        raise ValueError("Invalid value of the first_peak_polarity argument. Use \"positive\" or \"negative\".")
    return s


def sawtooth_pulse(sr, dur, amp, first_peak_polarity="positive"):
    """
    :param sr: sampling rate
    :param dur: duration in seconds
    :param amp: amplitude in μA
    :param first_peak_polarity: "positive" or "negative"
    :return: sawtooth pulse
    """
    t = np.arange(0, dur, 1.0 / sr)
    freq = 1.0 / dur
    s = sig.sawtooth(2 * np.pi * freq * t) * (amp / 2)
    if first_peak_polarity == "positive":
        pass
    elif first_peak_polarity == "negative":
        s *= -1
    else:
        raise ValueError("Invalid value of the first_peak_polarity argument. Use \"positive\" or \"negative\".")
    return s


def sin_pulse(sr, dur, amp, first_peak_polarity="positive"):
    """
    :param sr: sampling rate
    :param dur: duration in seconds
    :param amp: amplitude in μA
    :param first_peak_polarity: "positive" or "negative"
    :return: sinusoidal pulse
    """
    t = np.arange(0, dur, 1.0 / sr)
    freq = 1.0 / dur
    s = np.sin(2 * np.pi * freq * t) * (amp / 2)
    if first_peak_polarity == "positive":
        pass
    elif first_peak_polarity == "negative":
        s *= -1
    else:
        raise ValueError("Invalid value of the first_peak_polarity argument. Use \"positive\" or \"negative\".")
    return s
