import cv2
from video_frame_generator import video_frame_parser
from flicker_count_detector import flicker_counter


def main(): 

    capture = cv2.VideoCapture(r"C:\Users\PC\Downloads\Pokemon EP38 - Electric Soldier Porygon + ENG Subtitles - Trim.mp4") # tehcnically an array of numpyndarray (frames)

    frame_array, sliding_window_size = video_frame_parser(capture)
    print(frame_array)
    threshold = 16

    flicker_counter(frame_array, sliding_window_size, threshold)

if __name__ == '__ main __':
    main()