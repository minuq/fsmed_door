from subprocess import check_output, call
from datetime import datetime
from time import sleep
import os
import slack


def main():
    try:
        now = datetime.now().strftime("%H")
        print(now)
        custom_env = os.environ.copy()
        custom_env["DISPLAY"] = ":0"
        # 100% dumme Idee, aber funktioniert halt
        call(['sudo','-u','pidisplay','scrot','/tmp/mensa_{}.png'.format(now)],env=custom_env)
        call(['rsync','/tmp/mensa_{}.png'.format(now),'pi@134.130.18.217:/home/flinke/workspace/swag/config/www/slack/'])
        message = 'https://fsmed8.fsmed.rwth-aachen.de/mensa_{}.png'.format(now)
        slack.main("screen.ts","Clearing this up...")
        sleep(10)
        res = slack.main("screen.ts",message)
        print(res)
    except Exception as err:
        print(str("error: {0}".format(err)))