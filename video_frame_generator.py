# takes a video, decompiles it into different frames and then stores the raw pixel data. 

import cv2
from helper_function import luminance


capture = cv2.VideoCapture(r"C:\Users\PC\Downloads\Pokemon EP38 - Electric Soldier Porygon + ENG Subtitles - Trim.mp4") # tehcnically an array of numpyndarray (frames)

f = 0
last_frame_luminance = -1
flicker_count = 0
luminance_array = []

lp = 0 # left pointer for sliding window
rp = 0 # right pointer for sliding window

fps = int(capture.get(cv2.CAP_PROP_FPS))

sliding_window_size = max(60, fps) # at most looks a 60 frames per second. based off definition that flickering should be between 3 and 60 Hz. 



while(capture.isOpened()):
    ret, frame = capture.read() # frame shape is 480, 640, 3 so 480 height, 640 width, 3 colour channels

    if ret == False:
        break

    # frame should be an opencv2 image, which is a numpyndarray , giving pixle counts. append to a dataframe

    # want to analyse each frame in a sliding window maybe? determining the amount of drastic color switches in scene ex primarly red vs primarily blue and then comparing to 
    # to a thrsdhol amount set by scietnitsts 
    
    fh = frame.shape[0] # height
    fw = frame.shape[1] #width

    # timescale =  # what is 1 frame IN SECONDS WE TAKE FRAMERATE TO 
    

    # so we should determine average colour of a frame or the predominant colour. 

    # [[480x640],[],[]]

    # for each array in the nd

    average_frame_colour = frame.mean(axis=(0,1))

    # define what a flicker or a flash is 

    relative_luminance = luminance(average_frame_colour)

    # given relative_luminance, we compare with the last frame to determine if there was a flicker at the current frame. This is if contrast is above 3:1 threshold. 

    # case if we have max sliding window size
    if rp - lp >= sliding_window_size:


        

    # case if window size is not maxed out
    else: 
        if last_frame_luminance == -1: # this is the first frame analyzed so don't worry
            last_frame_luminance = relative_luminance
            rp += 1
            continue
        contrast_ratio = max(relative_luminance, last_frame_luminance) / min(relative_luminance, last_frame_luminance)


        if (contrast_ratio >= 3.0):
            flicker_count += 1
        rp += 1


    last_frame_luminance = relative_luminance
    





