import os, re
from datetime import datetime



displays = {
            'VGA': (640,480),
            'sVGA': (800,600),
            'XGA': (1024,768),
            'HD': (1280,720),
            'HD+': (1600,900),
            'FHD': (1920,1080),
            '1080p':(1920,1080),
            '2K':(2560,1440),
            '4K':(3840,2160)
            }


def getTimeStamp(showMS: bool = False):
    if showMS == True:
        return datetime.now().strftime('%Y-%m-%d--%H%M%S.%f')
    else:
        return datetime.now().strftime('%Y-%m-%d--%H%M%S')


def buildPath(path):
    if os.path.exists(path) == False:
        os.mkdir(path)
    else:
        new_path = path + " " + getTimeStamp()
        os.mkdir(new_path)
