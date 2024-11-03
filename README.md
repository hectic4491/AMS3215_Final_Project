# Simple-Synth
> A simple synthesizer built for Stony Brook Universities AMS 325: 'Computing and Programming Fundamentals in AMS' final project.

### FILES ###
This repository contains 3 .py files:

frequency_gen.py
  generates the dictionary of frequencies

oscillator.py
  is the signal generator function of the simple synth. default values can be adjusted from this function.
 
interface.py
  the main project file that builds the interface and calls the above two files
 
 
### HOW TO START ###


# Report #

Simple Synth


Simple Synth is a digital synthesizer built with python that uses wavetable synthesis to construct an audio signal. A wavetable is an array in memory which stores a fragment of a waveform. The benefit of using a wavetable is improved computation time, as the waveform is broken into smaller segments, called samples. The focus of this project was to practice audio signal methods, as well as application development. Special attention was given to the user interface, which is something I've never done before. This report details the construction and features of Simple Synth. The github repository can be found at: https://github.com/hectic4491/AMS_315_Final_Project.


First, some background on sound synthesis. Typical acoustic instruments, like a grand piano or acoustic guitar, create sound by vibrating strings. A vibrating string will vibrate in many directions and at different partial intervals, called harmonics. The lowest of these intervals is called the fundamental frequency and is typically the most dominantly audible note. In an electronic keyboard, recordings of other instruments, such as a piano, organ, or guitar, are stored in memory and then played when specific keys are struck. In a synthesizer, the actual signal is generated onboard with an oscillator and then further sculpted and adjusted through various other filters. 
A sine wave could be written as a periodic function of time, such that: 


where A is defined to be the amplitude in range of [0,1], f is the frequency of the sine wave in hertz, t is where the function evaluates at time t in seconds, and phi is the current phase of the waveform. For our purposes we let phi = 0, as the phase of the signal is preserved when indexing the wavetable.


Common devices that record and play sound don't necessarily capture and write/read audio at a continuous interval, instead the standardized 44.1Khz sample rate is used to record and playback sound. The frequency spectrum that humans hear at is between 20 to 20,000Hz. Because of a certain Nyquist–Shannon sampling theorem, the sampling frequency must be twice that of which we wish to hear, hence sampling at 44.1K, since it’s a little more than double that of the highest human audible frequency. 
With that in mind, we can begin looking at the code.


The module frequency_gen.py constructs a dictionary key_frequency_dict that contains the note names and related frequencies. To generate a list of frequencies that sound “nice” with one another, we use 12 tone equal temperament, i.e. we divide each octave of notes into 12 half steps. To do this we need a reference note frequency to help generate the other notes. The following formula illustrates the computation: 


Where fn is the desired frequency that is n half steps away from reference frequency f0 (f0 usually taken to be A4 = 440Hz) multiplied against the 12 tone equal temperament constant 12th root of 2. The dictionary data type was used as the code becomes very readable, as note names refer to their respective frequency.


Next the oscillator.py module was built to house the oscillator function. The oscillator function constructs a wavetable array with robust parameters. The function accepts frequency, duration, waveform, wavetable_length, user_gain, and sampling_rate as input parameters. The function works by first initializing an array of size wavetable_length. This can be thought of as the “resolution” of the generated array. Higher values like 512 or 1024 will produce more “clear” sounding signals at the expense of more computation times. Low values such as 16 or 32 produce more “distorted / low fidelity” sounding signals. Next we compute the wavetable of the input waveform function. Next we compute the actual signal array, whose length corresponds to the duration * sampling_rate. Next we initialize index and index_inc counter variables to help match align the phase of the signal to the wavetable. In this process different methods can be used to align the signal, my method was a simple np.floor truncation. This step can largely influence the quality of the waveform, and with more sophisticated methods can produce higher quality waveforms, for example taking a weighted sum of the two neighboring indices and assigning that value to the array. In researching methods the phrase “0th order interpolation” appeared, however I didn’t have time to implement this method. Lastly the signal is gain-adjusted down a few decibels by multiplying against the amplitude of the waveform, as the raw signal is a bit too loud. The parameter user_gain can be adjusted to raise or lower the volume to taste.


Lastly the program's interface was constructed using pygame. The module interface.py houses the main while is_running loop and handles user input. Pygame can be used to make basic interfaces and has a quick start guide in its documentation here. For my program I simply followed the quick start guide to construct the barebones of the interface. Then I created and adjusted the pygame_gui.elements.UIButtons and event handlers until they resembled and functioned like a keyboard bed. The special function key_press was created in this module to translate the signal created from the oscillator function into a readable audio data type that the pygame audio mixer can read. In earlier versions of the project, a .wav file was written and stored within the directory everytime the function ran, and then specifically called with the .play() method. This created a lot of unwanted file clutter. After some investigation I found some code on how to instead directly play audio from an ndarray data type, circumventing the egregious reading/writing of .wav files.


Additional features of the Simple Synth is the ability to change waveforms and sample resolution while running the program. Playing the sine wave at different resolutions gives a good demonstration of the sample resolution. Changing the resolution while engaging the sawtooth doesn't alter the sound in a noticeable way, but as a sawtooth is a more linear function to begin with, that may be expected, as the continuous change of the sine wave makes it more susceptible to low resolution distortion.


Originally I had planned to include more waveforms, such as a fourier transform of a square (or ‘pulse’) wave and a triangle wave. Moreover I had intended to include more user interface functionality, such as volume adjustment, high-pass filters, low-pass filters, a noise generator that could be mixed into the signal, and key presses to trigger events instead of mouse clicks. However while looking into pygame I realized I wouldn’t necessarily have enough time to learn the library and implement everything I wanted. Still I consider the project a success as the oscillator function is robust enough for further development, and the program runs without problems. I intend to develop the synth further as software development is something I want to seriously pursue.

  * to start the synth, run interface.py


### PACKAGES USED ###
packages needed:
  * numpy
  * pygame
  * pygame_gui
  

built in VScode
