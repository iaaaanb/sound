# Musical Notes Frequency Table
# Based on equal-tempered scale with A4 = 440 Hz
# Data sourced from musical reference tables

# Dictionary with note frequencies in Hz across octaves 0-8
NOTE_FREQUENCIES = {
    'C': {
        0: 16.35, 1: 32.70, 2: 65.41, 3: 130.81, 4: 261.63, 
        5: 523.25, 6: 1046.50, 7: 2093.00, 8: 4186.01
    },
    'C#': {
        0: 17.32, 1: 34.65, 2: 69.30, 3: 138.59, 4: 277.18,
        5: 554.37, 6: 1108.73, 7: 2217.46, 8: 4434.92
    },
    'Db': {  # Same as C# (enharmonic equivalent)
        0: 17.32, 1: 34.65, 2: 69.30, 3: 138.59, 4: 277.18,
        5: 554.37, 6: 1108.73, 7: 2217.46, 8: 4434.92
    },
    'D': {
        0: 18.35, 1: 36.71, 2: 73.42, 3: 146.83, 4: 293.66,
        5: 587.33, 6: 1174.66, 7: 2349.32, 8: 4698.63
    },
    'D#': {
        0: 19.45, 1: 38.89, 2: 77.78, 3: 155.56, 4: 311.13,
        5: 622.25, 6: 1244.51, 7: 2489.02, 8: 4978.03
    },
    'Eb': {  # Same as D# (enharmonic equivalent)
        0: 19.45, 1: 38.89, 2: 77.78, 3: 155.56, 4: 311.13,
        5: 622.25, 6: 1244.51, 7: 2489.02, 8: 4978.03
    },
    'E': {
        0: 20.60, 1: 41.20, 2: 82.41, 3: 164.81, 4: 329.63,
        5: 659.25, 6: 1318.51, 7: 2637.02, 8: 5274.04
    },
    'F': {
        0: 21.83, 1: 43.65, 2: 87.31, 3: 174.61, 4: 349.23,
        5: 698.46, 6: 1396.91, 7: 2793.83, 8: 5587.65
    },
    'F#': {
        0: 23.12, 1: 46.25, 2: 92.50, 3: 185.00, 4: 369.99,
        5: 739.99, 6: 1479.98, 7: 2959.96, 8: 5919.91
    },
    'Gb': {  # Same as F# (enharmonic equivalent)
        0: 23.12, 1: 46.25, 2: 92.50, 3: 185.00, 4: 369.99,
        5: 739.99, 6: 1479.98, 7: 2959.96, 8: 5919.91
    },
    'G': {
        0: 24.50, 1: 49.00, 2: 98.00, 3: 196.00, 4: 392.00,
        5: 783.99, 6: 1567.98, 7: 3135.96, 8: 6271.93
    },
    'G#': {
        0: 25.96, 1: 51.91, 2: 103.83, 3: 207.65, 4: 415.30,
        5: 830.61, 6: 1661.22, 7: 3322.44, 8: 6644.88
    },
    'Ab': {  # Same as G# (enharmonic equivalent)
        0: 25.96, 1: 51.91, 2: 103.83, 3: 207.65, 4: 415.30,
        5: 830.61, 6: 1661.22, 7: 3322.44, 8: 6644.88
    },
    'A': {
        0: 27.50, 1: 55.00, 2: 110.00, 3: 220.00, 4: 440.00,  # A4 = 440 Hz (reference)
        5: 880.00, 6: 1760.00, 7: 3520.00, 8: 7040.00
    },
    'A#': {
        0: 29.14, 1: 58.27, 2: 116.54, 3: 233.08, 4: 466.16,
        5: 932.33, 6: 1864.66, 7: 3729.31, 8: 7458.62
    },
    'Bb': {  # Same as A# (enharmonic equivalent)
        0: 29.14, 1: 58.27, 2: 116.54, 3: 233.08, 4: 466.16,
        5: 932.33, 6: 1864.66, 7: 3729.31, 8: 7458.62
    },
    'B': {
        0: 30.87, 1: 61.74, 2: 123.47, 3: 246.94, 4: 493.88,
        5: 987.77, 6: 1975.53, 7: 3951.07, 8: 7902.13
    }
}

def get_frequency(note, octave):
    """
    Get the frequency of a musical note in a specific octave.
    
    Args:
        note (str): Note name (e.g., 'A', 'C#', 'Bb')
        octave (int): Octave number (0-8)
    
    Returns:
        float: Frequency in Hz, or None if not found
    """
    if note in NOTE_FREQUENCIES and octave in NOTE_FREQUENCIES[note]:
        return NOTE_FREQUENCIES[note][octave]
    return None

def calculate_frequency(note, octave):
    """
    Calculate frequency using the equal temperament formula.
    This is an alternative method that calculates from A4 = 440 Hz.
    
    Args:
        note (str): Note name
        octave (int): Octave number
    
    Returns:
        float: Calculated frequency in Hz
    """
    # Note positions relative to A (A=0, A#=1, B=2, C=3, etc.)
    note_positions = {
        'A': 0, 'A#': 1, 'Bb': 1, 'B': 2, 'C': 3, 'C#': 4, 'Db': 4,
        'D': 5, 'D#': 6, 'Eb': 6, 'E': 7, 'F': 8, 'F#': 9, 'Gb': 9,
        'G': 10, 'G#': 11, 'Ab': 11
    }
    
    if note not in note_positions:
        return None
    
    # Calculate semitones from A4
    semitones = (octave - 4) * 12 + note_positions[note]
    
    # A4 = 440 Hz, each semitone = 2^(1/12) ratio
    frequency = 440.0 * (2 ** (semitones / 12.0))
    return round(frequency, 2)

# Common note shortcuts
MIDDLE_C = NOTE_FREQUENCIES['C'][4]  # 261.63 Hz
CONCERT_A = NOTE_FREQUENCIES['A'][4]  # 440.00 Hz (reference pitch)

# Example usage functions
def play_note(note, octave, duration=1.0):
    """
    Example function to generate and play a note using sounddevice.
    You'll need: import sounddevice as sd, import numpy as np
    """
    frequency = get_frequency(note, octave)
    if frequency is None:
        print(f"Note {note}{octave} not found")
        return
    
    # Uncomment these lines when you have sounddevice and numpy installed:
    # sample_rate = 44100
    # t = np.linspace(0, duration, int(sample_rate * duration), False)
    # wave = 0.3 * np.sin(2 * np.pi * frequency * t)
    # sd.play(wave, sample_rate)
    # sd.wait()
    
    print(f"Playing {note}{octave} at {frequency} Hz")

# Print some examples
if __name__ == "__main__":
    print("Musical Note Frequency Table")
    print("=" * 40)
    print(f"Middle C (C4): {MIDDLE_C} Hz")
    print(f"Concert A (A4): {CONCERT_A} Hz")
    print()
    
    # Print a few octaves of C major scale
    c_major = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    print("C Major Scale (Octave 4):")
    for note in c_major:
        freq = get_frequency(note, 4)
        print(f"{note}4: {freq} Hz")
    print()
    
    # Test the calculation function
    print("Verification using calculation:")
    print(f"A4 calculated: {calculate_frequency('A', 4)} Hz")
    print(f"C4 calculated: {calculate_frequency('C', 4)} Hz")