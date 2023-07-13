import os
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

def getTimeStamp():
    return datetime.now().strftime('%Y-%m-%d--%H%M%S')

def buildPath(path):
    if os.path.exists(path) == False:
        os.mkdir(path)
    else:
        path = nextPath(path)
        os.mkdir(path)

def nextPath(path):
    """Creates a candidate path name that will not conflict with indexed predecessors.
    Uses log(n) time algorithm to check existence of predecessor names (rather than
    using sequential iteration)

    Args:
        path (string): path

    Returns:
        string: next path
    """
    i = 1
    while os.path.exists(path + " " + str(i)):
        i = i * 2
    a, b = (i // 2, i)
    while a + 1 < b:
        c = (a + b ) // 2
        a, b = (c, b) if os.path.exists(path + " " + str(c)) else (a, c)
    return path + " " + str(b)