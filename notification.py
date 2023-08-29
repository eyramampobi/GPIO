from gpiozero import LED,Button
from signal import pause
from time import sleep
import requests

led = LED(27)

button = Button(2)

ifttt_webhook = "https://maker.ifttt.com/trigger/{}/json/with/key/cYdC1ypytgw6JpBPPQuTE6"

def trigger_event(event):
    return requests.get(ifttt_webhook.format(event))


while True: 
    sleep(1)
    print("Ready")
    if button.is_pressed and not led.is_lit:
        led.on()
        event_name: str = input("Enter an event name: ")
        req = trigger_event(event=event_name)
        if req.status_code == 200:
            print("Event trigger successful")
        else:
            print("Not successful")
            
    elif led.is_lit and button.is_pressed:
        print("Turning led off (Please wait 1 second)...")
        led.off()