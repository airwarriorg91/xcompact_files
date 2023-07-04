import pandas as pd
import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt


df = pd.read_csv('forces.csv')
"""plt.plot(df.Time[50000:55000],df.Drag[50000:55000], label='Drag')
#plt.plot(df.time[50000:55000],df.lift[50000:55000], color='red', label='Lift')
plt.axhline(0.6, color='black')
plt.axhline(-0.6, color='black')
plt.axvline(390.2326, color='black', label='y=390.2326')
plt.axvline(394.571, color='black', label='y=394.571')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Drag (N)')
plt.title("Flow over a cylinder at Re=300")
plt.show()

#doing fft to find the frequency"""
spectrum = fft.fft(df.Drag)
sr=len(spectrum)/(df.Time[len(df.Time)-1])
freq = fft.fftfreq(len(spectrum)) * sr
plt.plot(freq, abs(spectrum))
plt.xlabel('Freq (Hz)')
plt.ylabel('DFT Amplitude |X(freq)|')
plt.xlim([-0.4,0.4])
plt.axvline(0.20, label="0.20 Hz", color="black")
plt.title("Flow over a cylinder at Re=300 HR")
plt.legend()
plt.show()
#FFT_freq = 0.226"""