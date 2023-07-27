"""Module for testing time functions"""
__version__ = "0.0.1"

import os
from time import sleep
import datetime as dt

import tlogger as tl
import tutilities as tu

print("Loaded")

tl.logger.info("Test Initialized.")

folder_name = 'test'
# save_dir = tu.get_preferred_path(folder_name, 'Pullman', iterate_name=False)

is_sleeping = True
interval_seconds = 10
n = 0
i = 0
h, m = tu.get_hour_and_minute()

os.system('echo Program initialized')
while h < 18:
    if (m >= 0) & (m < 11) | (m >= 20) & (m < 31) | (m >= 40) & (m < 51):
        if is_sleeping == True:
            is_sleeping = False
            i = 0    
            os.system('echo Good Morning')
        os.system(f'echo {n}, {i}, -capture-, {dt.datetime.now()}')
        save_dir = tu.get_preferred_path(folder_name, 'Pullman', iterate_name=False)
        img_path = os.path.join(save_dir,'{}.txt'.format(tu.get_time_stamp()))
        f = open(img_path, "w")
        f.close()
    else:
        is_sleeping = True
        i = 0
        os.system(f'echo {n}, Sleeping, {dt.datetime.now()}')
    sleep(interval_seconds)
    h, m = tu.get_hour_and_minute()
    n += 1
    i += 1
os.system('echo Program exited.')
