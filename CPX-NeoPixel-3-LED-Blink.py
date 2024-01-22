# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Blink example for boards with ONLY a NeoPixel LED (e.g. without a built-in red LED).
Includes QT Py and various Trinkeys.
Requires two libraries from the Adafruit CircuitPython Library Bundle.
Download the bundle from circuitpython.org/libraries and copy the
following files to your CIRCUITPY/lib folder:
* neopixel.mpy
* adafruit_pixelbuf.mpy
Once the libraries are copied, save this file as code.py to your CIRCUITPY
drive to run it.
"""
import time
import board
import random
import neopixel

# Calls the circuit Python neopixel library, specifies the default board 
# pins for the Neopixels, and the number of neopixels to access.  Returns a 
# list 'pixels' of indexable neopixles
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.05)

## Time to wait during mutliple sections of loop
_delay_time = 0.1

while True:
    # Black out all pixels
    pixels.fill((0, 0, 0))
        
    time.sleep(_delay_time)
        
    # Color our pixels
    for i in range(0, 10):
        pixels[i] = (random.randrange(0, 256, 1), random.randrange(0, 256, 1), random.randrange(0, 256, 1))
        time.sleep(_delay_time)
        
    # Wait before moving to next iteration
    time.sleep(_delay_time)
