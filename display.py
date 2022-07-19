from subprocess import check_output
from datetime import datetime
import slack
import scrot


try:
    now = int(datetime.now().strftime("%H"))
    if (8 <= now <= 15):
        message = check_output(['vcgencmd', 'display_power', '1']).decode("utf-8")[-2] # we only need 0 or 1
    else:
        message = check_output(['vcgencmd', 'display_power', '0']).decode("utf-8")[-2] # we only need 0 or 1
    message = "Display status: {0}".format(message)
    tsfile = "display.ts"
    res = slack.main(tsfile,message)
    print(res)
except Exception as err:
    print(str("error: {0}".format(err)))

scrot.main()