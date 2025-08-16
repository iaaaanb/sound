from notes import NOTE_FREQUENCIES

import sounddevice as sd
import numpy as np




# Test - generate and play a beep
sample_rate = 44100
frequency = 440  # A note
duration = 3  # half second

t = np.linspace(0, duration, int(sample_rate * duration), False)
beep = 0.3 * np.sin(2 * np.pi * frequency * t)

def frequencyy(t):
    return frequency * (1 + np.sin(2 * np.pi * frequency / 880 * t))

def wuuuiiiiiuuuu(t):
    return 0.3 * np.sin(2 * np.pi * frequencyy(t) * t)



print("Playing test beep...")
sd.play(beep, sample_rate)
sd.wait()  # Wait for it to finish
print("Done!")