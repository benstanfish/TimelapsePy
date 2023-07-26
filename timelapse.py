import tlogger as tl
tl.logger.info(tl.lmsg[0])

try:
	from picamera2 import Picamera2, Preview
	from libcamera import Transform, controls
	import time, datetime
	import os, sys
	import tutilities as tu
	
	tl.logger.info(tl.lmsg[2])

	picam2 = Picamera2()
	picam2.still_configuration.main.size = tu.displays['4K']
	picam2.still_configuration.main.format = 'XBGR8888'
	picam2.still_configuration.transform = Transform(hflip=True, vflip=True)
	#picam2.still_configuration.align()
	picam2.configure('still')
	picam2.start()

	picam2.set_controls({"AfMode": controls.AfModeEnum.Manual, 
                      "LensPosition":0.0, 
                      "AeEnable": False, 
                      "AwbEnable": False, 
                      "FrameRate": 1.0})
	time.sleep(3)
	tl.logger.info(tl.lmsg[3])

	# User Inputs
	number_images = 5
	capture_interval = 1
	folder_name = 'timelapse'
	create_mp4 = False
	
	tl.logger.info(tl.lmsg[4])

	pictures_dir = os.path.join(os.path.expanduser('~'), 'Pictures')
	images_dir = tu.build_path(os.path.join(pictures_dir, folder_name))

	tl.logger.info(tl.lmsg[5].format(images_dir))
	tl.logger.info(tl.lmsg[6])
	
	for i in range(1,number_images + 1):
		img_path = os.path.join(images_dir,'{}.jpg'.format(tu.get_timestamp(True)))
		picam2.capture_file(img_path)
		percent_complete = ('{:.1%}'.format(i/(number_images))).rjust(7," ")
		status = " ".join([str(i), percent_complete, img_path])
		print(status)
		tl.logger.info(status)
		time.sleep(capture_interval)

	tl.logger.info(tl.lmsg[7])

	# Use ffmpeg to create mp4
	if create_mp4 == True:
		tl.logger.info(tl.lmsg[8])
		all_pics = images_dir + '/*.jpg'
		system('ffmpeg -framerate 24 -pattern_type glob -i "{}" -c:v libx264 -r 30 -y output-test.mp4'.format(all_pics))
		tl.logger.info(tl.lmsg[9])
	picam2.close()

except Exception as e:
	tl.logger.error(tl.lmsg[99],'division',exc_info=e)
	
finally:
	tl.logger.info(tl.lmsg[999])

