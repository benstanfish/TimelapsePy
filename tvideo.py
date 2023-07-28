# Make video with ffmpeg

from os import system

create_mp4 = True
images_dir = '/home/alex/Pictures/lapse'

# Use ffmpeg to create mp4
if create_mp4 == True:
	all_pics = images_dir + '/*.jpg'
	system(f'ffmpeg -framerate 24 -pattern_type glob -i "{all_pics}" -c:v libx264 -r 30 -y output.mp4')
