"""TimelapsePy utility for creating mp4 from time lapse photos using ffmpeg"""
__version__ = "0.0.5"
__author__ = "Ben Fisher"

print(f"tvideo.py <version {__version__}> imported.")

import os
import tutilities as utils
import tlogger as log
import usersettings as users

collected_images_directory = os.path.join(os.path.expanduser('~'),'Pictures', users.directory_name_for_images)
output_path = os.path.join(os.path.expanduser('~'), 'Videos', f'{users.video_name}.mp4')

# For command line documentation refer to https://ffmpeg.org/ffmpeg.html
try:
	log.logger.info(log.message['video_render'])
	all_pics = collected_images_directory + '/*.' + utils.get_file_format(users.image_file_format)
	os.system(f'ffmpeg -framerate {users.frame_rate} -pattern_type glob -i "{all_pics}" -c:v libx264 -y {output_path}')
except Exception as e:
	log.logger.error(log.message['error'], 'division', exc_info=e)
	print("An error occurred in rendering. Exiting tvideo.py.")
