# oscillator
# called to construct wavetable

import numpy as np

#sine_wave = np.sin
#square_wave = signal.square
#sawtooth_wave = signal.sawtooth
#triangle_wave = signal.sawtooth(t,width=0.5)

def oscillator(frequency=440, duration=1.5, waveform=np.sin, wavetable_length=64, user_gain=0, sampling_rate=44100):
    '''
    constructs an array of waveform at resolution "wavetable_length" to play for "duration" seconds.

    frequency : frequency of note
    duration : how long note will play ; must be float
    waveform : type of waveform to generate ; must be function
    wavetable_length : "resolution" of the waveform ; must be float
    user_gain : adjust the volume of sound ; try steps of +/- 2
    sampling_rate : sample rate of audio mixer
    '''

    wavetable = np.zeros(wavetable_length)

    # dividing the waveform into wavetable_length segment values
    for n in range (wavetable_length):
        wavetable[n] = waveform(2*np.pi*n / wavetable_length)

    # variables
    signal = np.zeros((int(duration) * sampling_rate))
    index = 0
    index_inc = frequency * wavetable_length / sampling_rate 

    # setting each increment of signal to pull from wavetable
    for n in range(signal.shape[0]):
        signal[n] = wavetable[int(np.floor(index))]
        index += index_inc
        index %= wavetable_length
    
    # reduce gain by 20 to prevent loudness
    # then allow user to adjust to preferance
    gain = -20 + user_gain
    amplitude = 10 **(gain / 20)
    signal *= amplitude

    return signal



