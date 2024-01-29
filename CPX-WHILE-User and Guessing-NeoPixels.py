import time
import board
import neopixel
import digitalio
from random import randint

def main():
    print("Starting Code Challenge\n")
    
    # list 'pixels' of indexable neopixels
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.01)
    pixels.fill((0, 0, 0))
    
    try:
        user_num = int(input("Please input a number from 1-10\n"))
    except ValueError:
        raise ValueError("ERROR: User did not enter a valid number!")
    
    if user_num > 10:
        user_num = 10
        
    if user_num < 1:
        user_num = 1
    
    user_num -= 1
    
    pixels[user_num] = (0, 255, 0)
    
    i = 0
    while i < 5:
        rand_num = randint(0, 9)

        if rand_num == user_num:
            pixels[rand_num] = (0, 0, 255)
            break
        else:
            pixels[user_num] = (0, 255, 0)
            pixels[rand_num] = (255, 0, 0)
            i += 1
            
        time.sleep(0.5)
        pixels.fill((0, 0, 0))
    
    time.sleep(2)
    
    if i < 5:
        print("\nI Win, I guessed your number in", i, "tries")
    else:
        print("\nYou Win, I did not guess your number in", i, "tries")
    
    # Stop using the NeoPixel pin so we can get a reference to it next time
    pixels.deinit()
    print("\nEnding Code Challenge")

main()