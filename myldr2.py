from gpiozero import LightSensor, PWMLED

sensor = LightSensor(18)
led = PWMLED(16)

while True:
    v = sensor.value
    print("ldr value: ",v)
    led.value = v