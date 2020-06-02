# popmaszyna
import sounddevice as sd
import numpy as np
import random
fs = 44100
tone_freq = 440
A_sig = 2
t = np.arange(0,0.8, 1/fs)
signal = A_sig * np.sin(2 * np.pi * tone_freq * t)
sd.play(signal, fs)
sd.wait()

fs = 34100
tone_freq =300
A_sig = 10
t = np.arange(0, 0.8, 1/fs)
signal = A_sig * np.sin(4 * np.pi * tone_freq * t)

sd.play(signal, fs)
sd.wait()
