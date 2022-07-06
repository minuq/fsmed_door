from gpiozero import LED, Button
from signal import pause
from time import sleep 
import requests
import slack
import secrets

def write(text,mode):
    f = open("/tmp/door.log",mode)
    f.write(text+"\n")
    f.close()
def on():
    res = requests.post(url_on)
    slack.main("door.ts","Door status: Open")
    write("Door open\n"+str(res),"a")
    res = ''
def off():
    res = requests.post(url_off)
    slack.main("door.ts","Door status: Closed")
    write("Door closed\n"+str(res),"a")
    res = ''

write("Log enabled","w")
slack.main("door.ts","Door status: unknown")
button = Button(4)
url_off = secrets.url_off
url_on = secrets.url_on
res = ''
button.when_pressed = off
button.when_released = on
pause()

