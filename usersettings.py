"""User input values for TimelapsePy"""
__version__ = "0.0.1"
__author__ = "Ben Fisher"
# DO NOT EDIT ABOVE THIS LINE

#======================================================================
#                      Settings for save locations
#======================================================================

absolute_path_for_images = '/home/pi/timelapses/tmp'
absolute_path_for_videos = '/home/pi/timelapses'
unique_directory_name = False  # Recommend keeping this default = False

#======================================================================
#                 Basic settings for capturing images
#======================================================================

interval_in_seconds_between_capture = 10
image_file_format = 'jpg'

capture_continuously = True

# To capture images daily between the following hours, set 
# capture_continuously = False, otherwise the following values
# are ignored. Use 24 hour format.
capture_start_hour = 4  # Inclusive
capture_end_hour = 18  # Exclusive


#======================================================================
#                    Camera configuration settings
#======================================================================

resolution = 'max'
image_format = 'default'

flip_horizontal = False
flip_vertical = False

override_default_focus_settings = False

# Focal modes are 'manual', 'automatic' and 'continuous'. Note that
# 'default' = 'manual'.
# Focal distance ranges from 0.1 cm (10) to infinity (0)
user_focus_mode = 'manual'
user_focal_distance = 0


#======================================================================
#                        Render to mp4 video
#======================================================================

create_mp4 = False
video_name = "video"
frame_rate = 24

# DO NOT EDIT BELOW THIS LINE
print(f"usersettings.py <version {__version__}> imported.")