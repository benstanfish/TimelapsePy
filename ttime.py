"""Module for testing time functions"""
__version__ = "0.0.1"

import os
from time import sleep
import datetime as dt

import tlogger as tl
import tutilities as tu

tl.logger.info("Test Initialized.")

is_sleeping = True
interval_seconds = 10
n = 0
i = 0
h, m = tu.get_hour_and_minute()

os.system('echo Program initialized')
while h < 16:
    if (m >= 0) & (m < 11) | (m >= 20) & (m < 31) | (m >= 40) & (m < 51):
        if is_sleeping == True:
            is_sleeping = False
            i = 0    
            os.system('echo Good Morning')
        os.system(f'echo {n}, {i}, <capture>, {dt.datetime.now()}')
    else:
        is_sleeping = True
        i = 0
        os.system(f'echo {n}, Sleeping, {dt.datetime.now()}')
    sleep(interval_seconds)
    h, m = tu.get_hour_and_minute()
    n += 1
    i += 1
os.system('echo Program exited.')
