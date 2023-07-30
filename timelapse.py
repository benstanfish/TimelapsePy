"""TimelapsePy main module"""
__version__ = "0.0.10"
__author__ = "Ben Fisher"

import tlogger as log
log.logger.info(log.message[0])
log.logger.info(log.message['log_start'])

try:
    import os
    from time import sleep
    import datetime as dt
    
    from picamera2 import Picamera2, Preview
    from libcamera import Transform, controls

    import usersettings as users
    import tutilities as util

    log.logger.info(log.message['imports'])

    picam2 = Picamera2()
    picam2.still_configuration.main.size = util.get_resolution(users.resolution)
    picam2.still_configuration.main.format = util.get_image_format(users.image_format)
    picam2.still_configuration.transform = Transform(hflip = users.flip_horizontal,
                                                     vflip = users.flip_horizontal)
    picam2.configure('still')
    log.logger.info(log.message['configuration'])
    
    picam2.start()
    log.logger.info(log.message['camera_start'])
    
    sleep(3)
    
    picam2.set_controls({"AfMode": util.get_focal_mode(users.user_focus_mode), 
                         "LensPosition": util.get_focal_distance(users.user_focal_distance)})
    log.logger.info(log.message['controls'])

    infinite_loop = True
    is_sleeping = True
    n = 0
    i = 0
    h, m = util.get_hour_and_minute()


    log.logger.info(log.message['loop_ready'])
    log.logger.debug(f'Continuous capture mode: {users.capture_continuously}')
    log.logger.debug(f'Capture start hour: {users.capture_start_hour}')
    log.logger.debug(f'Capture start hour: {users.capture_end_hour}')

    while infinite_loop == True:
        if (users.capture_continuously == True) | (users.capture_continuously == False & 
                                                  (h >= users.capture_start_hour & 
                                                   h < users.capture_end_hour)):
            if is_sleeping == True:
                is_sleeping = False
                i = 0    
                log.logger.info(log.message['awake'])
            
            save_dir = util.get_preferred_path(users.absolute_path_for_images, iterate_name = util.get_iterate_name(users.unique_directory_name))
            img_path = os.path.join(save_dir,f'{util.get_time_stamp()}.{util.get_file_format(users.image_file_format)}')
            
            picam2.capture_file(img_path)
            
            status = " ".join([str(n).rjust(6, " "), str(i).rjust(6, " "), str(dt.datetime.now()), img_path])
            os.system(f'echo {status}')
            log.logger.info("Capture event: " + status)       
        else:
            if is_sleeping == False:
                i = 0
                is_sleeping = True
                log.logger.info('sleep')
            os.system(f'echo {n}, Sleeping, {dt.datetime.now()}')
        sleep(users.interval_in_seconds_between_capture)
        h, m = util.get_hour_and_minute()
        n += 1
        i += 1
    os.system('Exiting program event loop.')
    log.logger.info(log.message['exit_loop'])
    
    if users.create_mp4 == True:
        # To run ffmpeg, it's recommended the tvideo.py script manually
        log.logger.info('User requested import of tvideo.py initiated.')
        import tvideo
        log.logger.info('User requested import of tvideo.py completed.')
    

except Exception as e:
	log.logger.error(log.message['error'], 'division', exc_info=e)
	
finally:
	log.logger.info(log.message['final'])
