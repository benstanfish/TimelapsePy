__version__ = "0.0.1"

import os
import getpass
from datetime import datetime

print(f"tutilities.py <version {__version__}> imported.")

displays = {
            'VGA': (640,480),
            'sVGA': (800,600),
            'XGA': (1024,768),
            'HD': (1280,720),
            'HD+': (1600,900),
            'FHD': (1920,1080),
            '1080p': (1920,1080),
            '2K': (2560,1440),
            '4K': (3840,2160),
            }

def get_timestamp(includeMs: bool = False):
    # LEGACY: Do not use for new projects
    if includeMs == True:
        return datetime.now().strftime('%Y%m%d--%H%M%S-%f')
    else:
        return datetime.now().strftime('%Y%m%d--%H%M%S')

def get_time_stamp():
    return datetime.now().strftime('%Y%m%d%H%M%S.%f')

def build_path(path):
    if os.path.exists(path) == False:
        os.mkdir(path)
    else:
        path = next_path(path)
        os.mkdir(path)
    return path

def next_path(path):
    """Creates a candidate path name that will not conflict with indexed predecessors. Uses log(n) time algorithm to check existence of predecessor names (rather than using sequential iteration)
    """
    i = 1
    while os.path.exists(path + " " + str(i)):
        i = i * 2
    a, b = (i // 2, i)
    while a + 1 < b:
        c = (a + b ) // 2
        a, b = (c, b) if os.path.exists(path + " " + str(c)) else (a, c)
    return path + " " + str(b)

def check_usb(drive_name):
    return os.path.exists('/media/' + getpass.getuser() + '/' + drive_name)

def get_preferred_path(directory_name, drive_name):
    usb_path = str('/media/' + getpass.getuser() + '/' + drive_name)
    if os.path.exists(usb_path) == True:
        path = build_path(os.path.join(usb_path, directory_name))
    else:
        path = build_path(os.path.join(os.path.join(os.path.expanduser('~'),'Pictures'), directory_name))
    return path
  
def get_hour_and_minute():
    now = dt.datetime.now()
    h = int(dt.datetime.strftime(now, "%H"))
    m = int(dt.datetime.strftime(now, "%M")) 
    return h, m