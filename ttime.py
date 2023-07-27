"""Module for testing time functions"""
__version__ = "0.0.1"

import tlogger as tl
tl.logger.info(tl.lmsg[0])

try:
    from picamera2 import Picamera2, Preview
    from libcamera import Transform, controls

    import os
    import sys
    from time import sleep
    import datetime as dt

    import tutilities as tu

    picam2 = Picamera2()
    picam2.still_configuration.main.size = tu.displays['4K']
    picam2.still_configuration.main.format = 'XBGR8888'
    picam2.still_configuration.transform = Transform(hflip=True, vflip=True)
    picam2.configure('still')
    picam2.start()

    picam2.set_controls({"AfMode": controls.AfModeEnum.Manual, 
                          "LensPosition":0.0, 
                          "AeEnable": False, 
                          "AwbEnable": False, 
                          "FrameRate": 1.0})
                          
    time.sleep(3)
    tl.logger.info(tl.lmsg[3])	

    folder_name = 'lapse'

    continue_running = True
    hello_joshua = True
    is_sleeping = True
    interval_seconds = 10
    n = 0
    i = 0
    h, m = tu.get_hour_and_minute()

    os.system('echo Program initialized')
    while continue_running == True:
        if (h >= 4 & h <= 22) | hello_joshua == True:
            if is_sleeping == True:
                is_sleeping = False
                i = 0    
                os.system('echo Good Morning')
            os.system(f'echo {n}, {i}, -capture-, {dt.datetime.now()}')
            save_dir = tu.get_preferred_path(folder_name, 'Pullman', iterate_name=False)
            img_path = os.path.join(save_dir,'{}.jpg'.format(tu.get_time_stamp()))
            
            picam2.capture_file(img_path)
            # percent_complete = ('{:.1%}'.format(i/(number_images))).rjust(7," ")
            status = " ".join([str(i), img_path])
            print(status)
            tl.logger.info(status)       
        else:
            is_sleeping = True
            i = 0
            os.system(f'echo {n}, Sleeping, {dt.datetime.now()}')
        sleep(interval_seconds)
        h, m = tu.get_hour_and_minute()
        n += 1
        i += 1
    os.system('echo Loop ended.')
    tl.logger.info("Loop has ended")
    
except Exception as e:
	tl.logger.error(tl.lmsg[99],'division',exc_info=e)
	
finally:
	tl.logger.info(tl.lmsg[999])
