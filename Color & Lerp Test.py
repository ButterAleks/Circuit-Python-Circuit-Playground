# Save on CPX/CPB as code.py

#
# Libraries
#

import time
import board
import digitalio
from adafruit_circuitplayground import cp

#led = digitalio.DigitalInOut(board.D13)
#led.direction = digitalio.Direction.OUTPUT

#
# Functions
#

def _lerp(a: float, b: float, t: float):
    return a + (b - a) * t

def _lerp_color(old_red, new_red, old_green, new_green, old_blue, new_blue, time_start, specified_time):
    # Multiply specified time by 1000000000 so that way it converts from nanoseconds to regular seconds
    return (_lerp(old_red, new_red, (time.monotonic_ns() - time_start) / (specified_time * 1000000000)),
            _lerp(old_green, new_green, (time.monotonic_ns() - time_start) / (specified_time * 1000000000)),
            _lerp(old_blue, new_blue, (time.monotonic_ns() - time_start) / (specified_time * 1000000000)))

#
# Variables
#

_specified_time = 1.5
_time_start = -1
_flip_flop = False

#
# Initalization
#

cp.pixels.brightness = 0.1

#
# Main Loop
#
ble = None
while True:
    if _time_start == -1:
        _time_start = time.monotonic_ns()
    
    for i in range(0, 10):
        if _flip_flop:
            if(i > 6):
                cp.pixels[i] = _lerp_color(0, 0, 0, 0, 0, 255, _time_start, _specified_time)
            elif(i > 3):
                cp.pixels[i] = _lerp_color(0, 0, 0, 255, 0, 0, _time_start, _specified_time)
            else:
                cp.pixels[i] = _lerp_color(0, 255, 0, 0, 0, 0, _time_start, _specified_time)
        else:
            if(i > 6):
                cp.pixels[i] = _lerp_color(0, 0, 0, 0, 255, 0, _time_start, _specified_time)
            elif(i > 3):
                cp.pixels[i] = _lerp_color(0, 0, 255, 0, 0, 0, _time_start, _specified_time)
            else:
                cp.pixels[i] = _lerp_color(255, 0, 0, 0, 0, 0, _time_start, _specified_time)            
    
    # Multiply specified time by 1000000000 so that way it converts from nanoseconds to regular seconds
    if time.monotonic_ns() - _time_start >= _specified_time * 1000000000:
        _time_start = -1
        _flip_flop = not _flip_flop
    
    
    if cp.button_a:print("Button A Pressed!")
    if cp.button_b:
        print("Button B Pressed!")