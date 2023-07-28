"""TimelapsePy utility for creating mp4 from time lapse photos using ffmpeg"""
__version__ = "0.0.1"
__author__ = "Ben Fisher"

import os
import tutilities as utils
import usersettings as users

create_mp4 = True
collected_images_directory = os.path.join((os.path.expanduser('~'),'Pictures'), users.directory_name_for_images)

# For command line documentation refer to https://ffmpeg.org/ffmpeg.html
if users.create_mp4 == True:
	all_pics = collected_images_directory + '/*.' + utils.get_file_format(users.image_file_format)
	os.system(f'ffmpeg -framerate {users.frame_rate} -pattern_type glob -i "{all_pics}" -codec:v libx264 -y {users.video_name}.mp4')

