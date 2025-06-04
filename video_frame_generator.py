# takes a video, decompiles it into different frames and then stores the raw pixel data. 

import cv2


capture = cv2.VideoCapture(r"C:\Users\PC\Downloads\Pokemon EP38 - Electric Soldier Porygon + ENG Subtitles - Trim.mp4") # tehcnically an array of numpyndarray (frames)

f = 0

fps = int(capture.get(cv2.CAP_PROP_FPS))
print(fps)


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

    


    





