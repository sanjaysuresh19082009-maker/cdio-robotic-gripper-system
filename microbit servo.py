from microbit import *
import music
from servo import Servo
from neopixel import NeoPixel
# IMPORTANT
# neopixel must be inserted in pin2
# claw must be inserted in pin1
# actuator must be inserted in pin8
num_pixels = 8
np = NeoPixel(pin2, num_pixels)
claw_pin=pin1
claw=Servo(claw_pin)
claw.write_angle(0)

actuator_pin=pin8
actuator=Servo(actuator_pin)
actuator.write_angle(0)

tunes={"open":["c4:2","e4:2","g4:4"],"close":["g4:2","e4:2","c4:2"]}

def light_open():
    for pixel in range(num_pixels):
        np[pixel]=(10,255,10)
        np.show()
        sleep(25) 

def light_close():
    for pixel in reversed(range(num_pixels)):
        np[pixel]=(0,0,0)
        np.show()
        sleep(25)
   
while True:
    if button_a.is_pressed():
        music.play(tunes["open"],wait=False)
        light_open()
        claw.write_angle(160)
        
            

    elif button_b.is_pressed():
        music.play(tunes["close"],wait=False)
        light_close()
        claw.write_angle(0)
        sleep(2000)
        actuator.write_angle(180)
        actuator.write_angle(0)
        actuator.write_angle(180)

        