#!/usr/bin/python3

import os.path
import os
import datetime
from tabulate import tabulate
from argparse import ArgumentParser
import warnings
from warnings import warn as warning

parser = ArgumentParser()
parser.add_argument( '-u', '--username', dest='username', default=None, help='Username to message' )
parser.add_argument( '-m', '--message', dest='message', default=None, help='Message')
parser.add_argument( '-c', '--channel', dest='channel', default=None, help='Channel to message')
results = parser.parse_args()

# @icaoberg Read secrets. assumes file exists in ~/.SLACK_SECRETS
from pathlib import Path
file = str(Path.home()) + os.sep + '.SLACK_SECRETS'
exec(open(file).read())

if results.username != None and results.channel == None:
	direct_message = True
	message_channel = False
else:
	direct_message = False
	message_channel = True

if direct_message:
	if results.username == 'icaoberg':
		url = DIRECT_MESSAGE_ICAOBERG
	else:
		url = DIRECT_MESSAGE_ICAOBERG

	command = 'curl -X POST -H \'Content-type: application/json\' --data \'{"type": "mrkdwn", "text":"' + results.message + '"}\' ' + url
	os.system(command)
	exit()

if message_channel:
	if results.channel == 'general':
		url = CHANNEL_GENERAL
	elif results.channel == 'admins':
		url = CHANNEL_ADMINS
	elif results.channel == 'computing':
		url = CHANNEL_COMPUTING
	elif results.channel == 'staff':
		url = CHANNEL_STAFF
	elif results.channel == 'social':
		url = CHANNEL_SOCIAL
	elif results.channel == 'faculty':
		url = CHANNEL_FACULTY
	elif results.channel == 'random':
		url = CHANNEL_RANDOM
	else:
		print('Channel not set or unknown. Publishing to general.')
		url = CHANNEL_GENERAL

	command = 'curl -X POST -H \'Content-type: application/json\' --data \'{"text":"' + results.message + '"}\' ' + url
	os.system(command)
	exit()
