import numpy as np
import soundfile as sf

flag, rate = sf.read('../htb/flag.wav')


# randomly shuffle the frequencies
freqs = np.fft.rfftfreq(len(flag), 1.0/rate)
filter_frequency_response = np.random.uniform(-10, 10, len(freqs))

# get the amplitudes
def filter(sample):
    amplitudes = np.fft.rfft(sample)
    shuffled_amplitudes = amplitudes * filter_frequency_response

    return np.fft.irfft(shuffled_amplitudes)

impulse = np.zeros(len(flag))
impulse[0] = 1

shuffled_signal = filter(impulse)
sf.write('impulse_response.wav', shuffled_signal, rate)

shuffled_flag = filter(flag)
sf.write('shuffled_flag.wav', shuffled_flag, rate)