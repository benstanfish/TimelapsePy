"""Logging functions for TimelapsePy"""
__version__ = "0.0.2"
__author__ = "Ben Fisher"

import logging

logger = logging.getLogger('TimelapsePy')
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

message = {
			0: "-" * 75,
			1: "",
			'log_start': 'Logger successfully initialized.',
			'imports': 'Imports successfully completed.',
			'configuration': 'Camera configurations completed.',
			'camera_start' : 'Camera started.',
			'controls': 'Camera controls set.',
			'loop_ready': 'Program will enter event loop now.',
			'awake': 'Event loop sleep cycle discontinued.',
			'sleep': 'Event loop has entered sleep cycle.',
			'exit_loop': 'Program is naturally exiting event loop.',
   			'error': "Error at %s",
			'final': "End of script. Program exiting."
		}

print(f"tlogger.py <version {__version__}> imported.")