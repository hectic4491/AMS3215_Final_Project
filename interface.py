# main program file
# run to open program
import pygame
import numpy as np
import pygame_gui
from frequency_gen import key_frequency_dict
from oscillator import oscillator


# init pygame
pygame.init()

# build window
pygame.display.set_caption('robs Simple_Synth')
window_surface = pygame.display.set_mode((900, 400))

background = pygame.Surface((900, 400))
background.fill(pygame.Color('#225500'))

manager = pygame_gui.UIManager((900, 400))

# octave3 white keys
c_3_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 200), (50, 150)), text='C3', manager=manager)
d_3_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((60, 200), (50, 150)), text='D3', manager=manager)
e_3_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((110, 200), (50, 150)), text='E3', manager=manager)
f_3_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((160, 200), (50, 150)), text='F3', manager=manager)
g_3_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((210, 200), (50, 150)), text='G3', manager=manager)
a_4_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((260, 200), (50, 150)), text='A4', manager=manager)
b_4_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((310, 200), (50, 150)), text='B4', manager=manager)

# octave3 black keys
c_sharp_3_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((35, 40), (50, 150)), text='C#3', manager=manager)
d_sharp_3_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((85, 40), (50, 150)), text='D#3', manager=manager)
f_sharp_3_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((185, 40), (50, 150)), text='F#3', manager=manager)
g_sharp_3_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((235, 40), (50, 150)), text='G#3', manager=manager)
a_sharp_4_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((285, 40), (50, 150)), text='A#4', manager=manager)

# octave4 white keys
c_4_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((360, 200), (50, 150)), text='C4', manager=manager)
d_4_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((410, 200), (50, 150)), text='D4', manager=manager)
e_4_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((460, 200), (50, 150)), text='E4', manager=manager)
f_4_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((510, 200), (50, 150)), text='F4', manager=manager)
g_4_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((560, 200), (50, 150)), text='G4', manager=manager)
a_5_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((610, 200), (50, 150)), text='A5', manager=manager)
b_5_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((660, 200), (50, 150)), text='B5', manager=manager)

# octave4 black keys
c_sharp_4_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((385, 40), (50, 150)), text='C#4', manager=manager)
d_sharp_4_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((435, 40), (50, 150)), text='D#4', manager=manager)
f_sharp_4_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((535, 40), (50, 150)), text='F#4', manager=manager)
g_sharp_4_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((585, 40), (50, 150)), text='G#4', manager=manager)
a_sharp_5_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((635, 40), (50, 150)), text='A#5', manager=manager)

# waveform buttons
sine_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((790,20), (100,50)), text='SINE WAVE', manager=manager)
saw_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((790,80), (100,50)), text='SAW WAVE', manager=manager)
# square_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((790,140), (100,50)), text='SQR WAVE', manager=manager)

# wavetable size buttons
res16_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((740,260), (50,40)), text='16', manager=manager)
res32_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((790,260), (50,40)), text='32', manager=manager)
res64_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((840,260), (50,40)), text='64', manager=manager)

res128_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((740,300), (50,40)), text='128', manager=manager)
res256_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((790,300), (50,40)), text='256', manager=manager)
res512_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((840,300), (50,40)), text='512', manager=manager)


clock = pygame.time.Clock()
is_running = True

# turns signal array into readable audio data and plays sound
def key_press(note):
    '''
    turns signal array into readable audio data
    '''
    signal = np.asarray([32767*note, 32767*note]).T.astype(np.int16)
    signal = pygame.sndarray.make_sound(signal.copy())
    return signal.play()


#waveform types
#init
user_wave = np.sin
#choices
sine_wave = np.sin
def sawtooth(x):
    return (x + np.pi) / np.pi % 2 - 1


#resolution types
#only really noticable on sine wave
#init
user_resolution = 64
#choices
res16 = 16
res32 = 32
res64 = 64
res128 = 128
res256 = 256
res512 = 512


# main loop
while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        

        # waveform button events
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == sine_button:
                user_wave = sine_wave
        
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == saw_button:
                user_wave = sawtooth

        #if event.type == pygame_gui.UI_BUTTON_PRESSED:
        #    if event.ui_element == square_button:
        #        user_wave = square_wave


        # resolution button events
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == res16_button:
                user_resolution = res16
        
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == res32_button:
                user_resolution = res32

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == res64_button:
                user_resolution = res64

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == res128_button:
                user_resolution = res128

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == res256_button:
                user_resolution = res256

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == res512_button:
                user_resolution = res512


        # piano key press events
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == c_3_button:
                key_press(oscillator(key_frequency_dict['C3'], waveform=user_wave, wavetable_length=user_resolution))

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == c_sharp_3_button:
               key_press(oscillator(key_frequency_dict['C#3'], waveform=user_wave, wavetable_length=user_resolution))

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == d_3_button:
                key_press(oscillator(key_frequency_dict['D3'], waveform=user_wave, wavetable_length=user_resolution))


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == d_sharp_3_button:
                key_press(oscillator(key_frequency_dict['D#3'], waveform=user_wave, wavetable_length=user_resolution))


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == e_3_button:
                key_press(oscillator(key_frequency_dict['E3'], waveform=user_wave, wavetable_length=user_resolution))


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == f_3_button:
                key_press(oscillator(key_frequency_dict['F3'], waveform=user_wave, wavetable_length=user_resolution))


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == f_sharp_3_button:
                key_press(oscillator(key_frequency_dict['F#3'], waveform=user_wave, wavetable_length=user_resolution))


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == g_3_button:
                key_press(oscillator(key_frequency_dict['G3'], waveform=user_wave, wavetable_length=user_resolution))


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == g_sharp_3_button:
                key_press(oscillator(key_frequency_dict['G#3'], waveform=user_wave, wavetable_length=user_resolution))


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == a_4_button:
                key_press(oscillator(key_frequency_dict['A4'], waveform=user_wave, wavetable_length=user_resolution))


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == a_sharp_4_button:
                key_press(oscillator(key_frequency_dict['A#4'], waveform=user_wave, wavetable_length=user_resolution))


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == b_4_button:
                key_press(oscillator(key_frequency_dict['B4'], waveform=user_wave, wavetable_length=user_resolution))


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == c_4_button:
                key_press(oscillator(key_frequency_dict['C4'], waveform=user_wave, wavetable_length=user_resolution))


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == c_sharp_4_button:
                key_press(oscillator(key_frequency_dict['C#4'], waveform=user_wave, wavetable_length=user_resolution))


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == d_4_button:
                key_press(oscillator(key_frequency_dict['D4'], waveform=user_wave, wavetable_length=user_resolution))


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == d_sharp_4_button:
                key_press(oscillator(key_frequency_dict['D#4'], waveform=user_wave, wavetable_length=user_resolution))


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == e_4_button:
                key_press(oscillator(key_frequency_dict['E4'], waveform=user_wave, wavetable_length=user_resolution))


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == f_4_button:
                key_press(oscillator(key_frequency_dict['F4'], waveform=user_wave, wavetable_length=user_resolution))


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == f_sharp_4_button:
                key_press(oscillator(key_frequency_dict['F#4'], waveform=user_wave, wavetable_length=user_resolution))


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == g_4_button:
                key_press(oscillator(key_frequency_dict['G4'], waveform=user_wave, wavetable_length=user_resolution))


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == g_sharp_4_button:
                key_press(oscillator(key_frequency_dict['G#4'], waveform=user_wave, wavetable_length=user_resolution))


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == a_5_button:
                key_press(oscillator(key_frequency_dict['A5'], waveform=user_wave, wavetable_length=user_resolution))


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == a_sharp_5_button:
                key_press(oscillator(key_frequency_dict['A#5'], waveform=user_wave, wavetable_length=user_resolution))


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == b_5_button:
                key_press(oscillator(key_frequency_dict['B5'], waveform=user_wave, wavetable_length=user_resolution))



        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()