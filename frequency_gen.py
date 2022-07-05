# generate a dictionary of notes and their frequencies
# fn = f0 * (a) ** n
# where fn is desired frequency n half-steps away from
# fixed note f0 (taken to be A4 : 440Hz)
# (a) is 12 note equal temperment constant of 12th root of 2

a = (2)**(1/12)

key_frequency_dict = {
    'C3':0,
    'C#3':0,
    'D3':0,
    'D#3':0,
    'E3':0,
    'F3':0,
    'F#3':0,
    'G3':0,
    'G#3':0,
    'A4':0,
    'A#4':0,
    'B4':0,
    'C4':0,
    'C#4':0,
    'D4':0,
    'D#4':0,
    'E4':0,
    'F4':0,
    'F#4':0,
    'G4':0,
    'G#4':0,
    'A5':0,
    'A#5':0,
    'B5':0,
    }

n = -9
for k, v in key_frequency_dict.items():
    key_frequency_dict[k] = (440*a**n)
    n += 1
print(key_frequency_dict)