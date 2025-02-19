#!/usr/bin/python3
# -*- coding: utf-8 -*-

import configparser
import os
import subprocess
import sys
from datetime import date

# We want load first current location
CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
if CURRENT_PATH not in sys.path:
    sys.path = [CURRENT_PATH] + sys.path
import utils

USER_NAME = utils.get_user()
HOMEDIR = os.path.expanduser('~{}'.format(USER_NAME))

_ = utils.load_translation('preferences')

config_file = HOMEDIR + '/.config/slimbookbattery/slimbookbattery.conf'

config = configparser.ConfigParser()
config.read(config_file)

cmd = (subprocess.getstatusoutput("cat /sys/class/power_supply/BAT0/status"))

if cmd[0] == 0:
    status = cmd[1]

    if status == 'Discharging':
        config.set('CONFIGURATION', 'plugged', str(date.today()))
        configfile = open(config_file, 'w')
        config.write(configfile)
        configfile.close()

else:
    status = (_('Unknown'))

print(status)
