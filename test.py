import numpy as np

f = 100
fs = 44100
t = np.arange(0,fs)/fs
signal = np.sin(2*np.pi*f*t)