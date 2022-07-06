from subprocess import check_output
import slack

try:
    ip = check_output(['hostname', '--all-ip-addresses'])
    slack.main("mensa.ts","ip: {0}".format(ip.decode("utf-8")))
except Exception as err:
    print(str("error: {0}".format(err)))
