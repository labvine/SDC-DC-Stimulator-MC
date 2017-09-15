# Created by pdzwiniel at 2017-09-15.
# Contact: piotr.dzwiniel@gmail.com.
# This file is a part of SDC-DC-Stimulator-MC project.

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
