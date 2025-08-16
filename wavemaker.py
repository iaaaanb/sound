import sounddevice as sd
import numpy as np
from notes import NOTE_FREQUENCIES

SAMPLE_RATE = 44100

class Wave:
    def __init__(self, note : str, octave : int, amplitude = 0.3):
        self.note = note
        self.octave = octave
        self.frequency = NOTE_FREQUENCIES[note][octave]
        self.amplitude = amplitude

    def wave(self, start : float, stop : float):
        t = np.linspace(start, stop, SAMPLE_RATE*(stop-start), False)
        wave = self.amplitude*np.sin(2*np.pi*self.frequency*t)
        return wave
    
    def wave_dur(self, duration):
        t = np.linspace(0,duration, SAMPLE_RATE*duration, False)
        return self.amplitude*np.sin(2*np.pi*self.frequency*t)


do4 = Wave("C", 4)

for octave in range(8):
    for note in NOTE_FREQUENCIES:
        sd.play(Wave(note,octave).wave_dur(1), SAMPLE_RATE)

sd.wait()

