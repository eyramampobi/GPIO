from gpiozero import LED,Button
from signal import pause
from time import sleep

greenled = LED(17)
redled = LED(27)
yellowled = LED(22)
button = Button(2)

def traffic():
        greenled.off()
        
        for a in range(0,4):
            yellowled.on()
            sleep(1)
            yellowled.off()
            sleep(1)
        
        redled.on()
        sleep(5)
        redled.off()
        greenled.on()
        sleep(5)

button.when_pressed = traffic
    
    
