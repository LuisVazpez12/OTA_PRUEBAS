import machine,time
from machine import Pin 

led= Pin(2,Pin.OUT)
led.on()
time.sleep_ms(800)
led.off()
time.sleep_ms(800)

