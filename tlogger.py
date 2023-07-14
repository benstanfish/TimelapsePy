print('tlogger.py successfully imported')

import logging

logger = logging.getLogger('timelapsepy')
logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler('tl.log')
fileHandler.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fileHandler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)

logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)

lmsg = {
		0: "-"*75,
		1: "",
		2: "TimelapsePy script initialized",
		3: "imports complete",
		4: "parameters set",
		5: "directory path built: {}",
		6: "image capture cycle initialized",
		7: "image capture cycle completed",
		8: "image to video render initialized",
		9: "video rendering complete",
		99: "error at %s",
		999: "end of script"
		}

