from subprocess import check_output
import json
import requests
import os.path
from datetime import datetime
import secrets

token = secrets.token
channel = secrets.channel
username = secrets.username
icon_emoji= secrets.icon_emoji


def post_to_slack(text):
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': token,
        'channel': channel,
        'text': text,
        'icon_emoji': icon_emoji,
        'username': username
    }).json()

def update_slack(text,ts):
    return requests.post('https://slack.com/api/chat.update', {
        'token': token,
        'channel': channel,
        'text': text,
        'ts': ts,
        "as_user": True
    }).json()


def main(tsfile,message):
    message = "("+datetime.now().strftime("%d.%m.%Y - %H:%M:%S")+") » "+message
    try:
        if (os.path.isfile(tsfile)):
            f = open("/home/pi/fsdoor/"+tsfile,"r")
            ts = f.read()
            res = update_slack("{0}".format(message),str(ts))
            print(res)
            f.close()
        else: 
            res = post_to_slack("{0}".format(message))
            f = open("/home/pi/fsdoor/"+tsfile,"w")
            f.write(res["ts"])
            print(res)
            f.close()
        return True
    except Exception as err:
        print(str("error: {0}".format(err)))
        return False
