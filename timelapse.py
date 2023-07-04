"""Library that simplifies Raspberry Pi Camera time lapse photography and conversion to video format."""
__author__ = "Ben Fisher"
__version__ = "0.0.1"
__license__ = "GPL"
__credits__ = ["Ben Fisher"]
__status__ = "Development"
__maintainer__ = "Ben Fisher"

from picamera2 import Picamera2, Preview
from libcamera import Transform, controls
import time
import os
from datetime import datetime, timedelta

picam2 = Picamera2()
picam2.preview_configuration.main.size = (3840,2160)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.transform = Transform(hflip=1,vflip=1)
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

picam2.set_controls({"AfMode":controls.AfModeEnum.Manual, "LensPosition":0.0})

# User Inputs
number_images = 48
capture_interval = 0.25
images_dir_name = 'timelapse4'
create_mp4 = False

pictures_dir = os.path.join(os.path.expanduser('~'),'Pictures')
images_dir = os.path.join(pictures_dir,images_dir_name)

for i in range(1,number_images + 1):
	img_path = os.path.join(images_dir,'img-{0:04d}.jpg'.format(i))
	picam2.capture_file(img_path)
	print(i, '{:.1%}'.format(i/(number_images)), img_path)
	time.sleep(capture_interval)


# Use ffmpeg to create mp4
if create_mp4 == True:
	all_pics = images_dir + '/*.jpg'
	system('ffmpeg -framerate 24 -pattern_type glob -i "{}" -c:v libx264 -r 30 -y output-test.mp4'.format(all_pics))
picam2.close()
