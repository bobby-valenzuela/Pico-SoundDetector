from machine import Pin
import utime

led_list = [i for i in range(0,20) ]
leds = [Pin(i,Pin.OUT) for i in led_list]
mic = Pin(15,Pin.IN)

def flash_leds():
#    while True:

    
    print(led_list)

    # on
    for n in led_list:
        leds[n].value(1)
        utime.sleep_ms(10)
    # off    
    for n in led_list:
        leds[n].value(0)
        utime.sleep_ms(10)
        


if __name__ == '__main__':
    
    while True:
        mic_val = mic.value()
        print("Current: " + str(mic_val))
        
        if mic_val:
            flash_leds()
        
        utime.sleep_ms(10)
