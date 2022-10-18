"""

Python code

"""
basic.show_icon(IconNames.HEART)
music.set_volume(255)
pins.analog_set_pitch_pin(AnalogPin.P0)
d = 1000
SA = 256
RE = SA * (9 / 8)
GA = RE * (10 / 9)
MA = GA * (16 / 15)
PA = MA * (9 / 8)
DHA = PA * (10 / 9)
NI = DHA * (9 / 8)
SA2 = NI * (16 / 15)
basic.pause(50)
music.set_volume(127)

def on_forever():
    pins.analog_pitch(SA, d)
    pins.analog_pitch(RE, d)
    pins.analog_pitch(GA, d)
    pins.analog_pitch(MA, d)
    pins.analog_pitch(PA, d)
    pins.analog_pitch(DHA, d)
    pins.analog_pitch(NI, d)
    pins.analog_pitch(SA2, d)
    basic.pause(50)
    pins.analog_pitch(SA2, d)
    pins.analog_pitch(NI, d)
    pins.analog_pitch(DHA, d)
    pins.analog_pitch(PA, d)
    pins.analog_pitch(MA, d)
    pins.analog_pitch(GA, d)
    pins.analog_pitch(RE, d)
    pins.analog_pitch(SA, d)
basic.forever(on_forever)
