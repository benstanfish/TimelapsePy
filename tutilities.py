"""Utility functions for TimelapsePy"""
__version__ = "0.0.3"
__author__ = "Ben Fisher"

from libcamera import controls

import os
import getpass
import datetime as dt

resolutions = {
                'vga': (640,480),
                'svga': (800,600),
                'xga': (1024,768),
                'hd': (1280,720),
                'hd+': (1600,900),
                'fhd': (1920,1080),
                '1080p': (1920,1080),
                '2k': (2560,1440),
                '4k': (3840,2160),
                'max': (4608,2592),
                'default': (4608,2592)
                }

image_formats = {
                'xbgr8888': 'XBGR8888',
                'xrgb8888': 'XRBG8888',
                'bgr888': 'BGR888',
                'rgb888': 'RGB888',
                'default': 'BGR888'
                }

focal_modes = {
                'default': controls.AfModeEnum.Manual,
                'manual': controls.AfModeEnum.Manual,
                'automatic': controls.AfModeEnum.Auto,
                'continuous': controls.AfModeEnum.Continuous                
                }

file_formats = {
                'jpg': 'jpg',
                'jpeg': 'jpg',
                'png': 'png',
                'bmp': 'bmp',
                '.jpg': 'jpg',
                '.jpeg': 'jpg',
                '.png': 'png',
                '.bmp': 'bmp',
                'default': 'jpg'
                }

def get_resolution(resolution: str):
    try:
        return resolutions[resolution.lower()]
    except KeyError:
        return resolutions['max']

def get_image_format(format: str):
    try:
        return image_formats[format.lower()]
    except KeyError:
        return image_formats['default']
        
def get_image_quality(quality: int):
    if quality < 0:
        return 0
    elif quality > 100:
        return 100
    else:
        return quality

def get_focal_mode(focal_mode: str):
    try:
        return focal_modes[focal_mode.lower()]
    except KeyError:
        return focal_modes['default']   

def get_focal_distance(focal_distance: float):
    if focal_distance <= 0.0:
        return 0
    elif focal_distance >= 10.0:
        return 10
    else:
        return focal_distance

def get_file_format(file_format: str):
    try:
        return file_formats[file_format.lower()]
    except KeyError:
        return file_formats['jpg']   
    
def get_iterate_name(iterate_name: bool):
    try:
        return iterate_name
    except:
        return False

def get_time_stamp():
    return dt.datetime.now().strftime('%Y%m%d.%H%M%S.%f')

def build_path(path, iterate_name = False):
    if os.path.exists(path) == False:
        os.mkdir(path)
    elif iterate_name == True:
        path = next_path(path)
        os.mkdir(path)
    return path

def next_path(path):
    """Creates a candidate path name that will not conflict with indexed predecessors. 
    Uses log(n) time algorithm to check existence of predecessor names (rather than using sequential iteration)
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

def get_preferred_path(directory_name, drive_name, iterate_name = False):
    usb_path = str('/media/' + getpass.getuser() + '/' + drive_name)
    if os.path.exists(usb_path) == True:
        path = build_path(os.path.join(usb_path, directory_name), iterate_name)
    else:
        path = build_path(os.path.join(os.path.join(os.path.expanduser('~'),'Pictures'), directory_name), iterate_name)
    return path
  
def get_hour_and_minute():
    now = dt.datetime.now()
    h = int(dt.datetime.strftime(now, "%H"))
    m = int(dt.datetime.strftime(now, "%M")) 
    return h, m

print(f"tutilities.py <version {__version__}> imported.")