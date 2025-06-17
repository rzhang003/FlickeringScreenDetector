import cv2
from video_frame_generator import video_frame_parser
from flicker_count_detector import flicker_counter
from video_segment_player import play_video_segment
import time

def main(): 


    #path = r"C:\Users\PC\Downloads\ScreenRecording_06-08-2025_14-07-25_1.mov"

    path = r"C:\Users\PC\Downloads\Pokemon EP38 - Electric Soldier Porygon + ENG Subtitles.mp4"
    capture = cv2.VideoCapture(path) # tehcnically an array of numpyndarray (frames)
    start = time.time() 
    frame_array, sliding_window_size = video_frame_parser(capture)
    end = time.time() 
    print(f"finished first part in {end-start} time")

    threshold = 16

    start = time.time() 
    trigger_sections = flicker_counter(frame_array, sliding_window_size, threshold)
    end = time.time() 
    print(f"finished second part in {end-start} time")
    for section in trigger_sections:
        input("Press Enter for next section...")
        play_video_segment(capture, section[0], section[1], 100)
        capture.release()
        
    

if __name__ == '__main__':
    print(4)
    main()

    