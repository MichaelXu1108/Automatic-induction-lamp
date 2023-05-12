from machine import Pin
from time import sleep

relay = Pin(26, Pin.OUT)
pir = Pin(33, Pin.IN)

while True:
    if pir():
        print("PIR ON")
        relay.on()
        sleep(5)
    
    if not pir():
        print("PIR OFF")
        relay.off()
        sleep(1)
