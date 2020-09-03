import numpy as np
import sounddevice as sd
import time


class Sound:
    frequencies: list
    duration: int
    samples_per_sec: int

    def __init__(self, frequencies, duration, sample_rate):
        self.frequencies = frequencies
        self.duration = duration
        self.sample_rate = sample_rate

    def freq_to_waveform(self, attenuation):
        chord = 0
        for frequency in self.frequencies:
            each_sample_number = np.arange(self.duration * self.sample_rate)
            waveform_raw = np.sin(2 * np.pi * each_sample_number * frequency / self.sample_rate)
            waveform_quiet = waveform_raw * attenuation
            chord = chord + waveform_quiet
        return chord


def play_sound(waveform, duration):
    sd.play(waveform)
    time.sleep(duration)
    sd.stop()


if __name__ == "__main__":
    freq = [440, 554.37, 659.25]  # [A, Cs, E]
    duration = 2  # in seconds
    fs = 44000
    snd = Sound(freq, duration, fs)

    atten = 0.3
    waveform = snd.freq_to_waveform(attenuation=atten)

    play_sound(waveform, duration)
