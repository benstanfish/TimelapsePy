

def capture_time(image_count: int, capture_interval: float):
    """Calculates time to capture all images in seconds.

    Args:
        image_count (int): number of images to capture
        capture_interval (float): time between successive capture in seconds

    Returns:
        (float): total time to capture all images in seconds.
    """
    return (image_count-1)*capture_interval

def video_duration(image_count: int, frames_per_second: float):
    """Calculates the total length of rendered video in seconds.

    Args:
        image_count (int): number of images captured
        frames_per_second (float): rendered frames per second.

    Returns:
        (float): total duration of rendered video in seconds.
    """
    try:
        return image_count/frames_per_second
    except ZeroDivisionError:
        print("Frames per second cannot be zero.")
   

def capture_interval(capture_time: float, video_duration: float, frames_per_second: float = 24):
    try:
        return capture_time/(video_duration*frames_per_second - 1)
    except ZeroDivisionError:
        print("Frames per second cannot be zero.")
        
def render_fps(capture_time: float, capture_interval: float, video_duration: float):
    try:
        return ((capture_time/capture_interval)+1)/video_duration
    except ZeroDivisionError:
        print("Capture interval and video duration cannot be zero.")
        
        
def estimate_file_size(width, height, bit_depth, units_KiB = True):
    """Estimate individual image file size

    Args:
        width (float): image width in pixels
        height (float): image height in pixels
        bit_depth (int): image color bit-depth

    Returns:
        float: Returns estimated image file size in kiB.
    """
    if units_KiB == True:
        return height * width * bit_depth / (8 * 2**10)
    else:
         return height * width * bit_depth / (8000)

def estimate_total_size(image_count, width, height, bit_depth, units_MiB = True):
    """Calculates total space required to store all images.

    Args:
        image_count (int): total number of images captured
        width (float): image width in pixels
        height (float): image height in pixels
        bit_depth (int): image color bit-depth

    Returns:
        float: Returns estimated image file size in MiB
    """
    if units_MiB == True:
        return image_count * height * width * bit_depth / (8 * 2**10) / 1000
    else:
         return image_count * height * width * bit_depth / (8000000)