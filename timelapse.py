"""Library that simplifies Raspberry Pi Camera time lapse photography and conversion to video format."""
__author__ = "Ben Fisher"
__version__ = "0.0.1"
__license__ = "GPL"
__credits__ = ["Ben Fisher"]
__status__ = "Development"
__maintainer__ = "Ben Fisher"

from picamera2 import Picamera2, Preview
from libcamera import Transform
import time
from os import system

picam = Picamera2()
config = picam.create_preview_configuration(transform=Transform(hflip=1,
vflip=1))
#config["transform"] = Transform(hflip=1,vflip=1)
picam.configure(config)

#picam.start_preview(Preview.QTGL)
picam.start()

for i in range(1,600):
	picam.capture_file('/home/ben/Pictures/timelapse/img-{0:04d}.jpg'.format(i))
	time.sleep(5)

picam.close()

# use ffmpeg to convert to a gif
system('ffmpeg -framerate 10 -pattern_type glob -i '\\home\\ben\\Pictures\\timelapse\\*.jpg' -c:v libx264 -r 30 output.mp4')
