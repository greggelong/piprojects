from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)
b =0
i = 0.1
while True:
    if b =< 1:

        led.value = b

        sleep(1)

        b = b +i 
    else:
        b =  0 
    