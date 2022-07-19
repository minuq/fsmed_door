from subprocess import check_output, call
from datetime import datetime
import slack

try:
    now = int(datetime.now().strftime("%H"))
    call(['DISPLAY=:0','scrot','/home/pidisplay/mensa_{}'.format(now)])
    f = open("/home/pidisplay/mensa_{}".format(now),"r")
    res = slack.upload_image(img)
    print(res)
except Exception as err:
    print(str("error: {0}".format(err)))
