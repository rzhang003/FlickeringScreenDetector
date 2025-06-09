import cv2
from video_frame_generator import video_frame_parser
from flicker_count_detector import flicker_counter


def main(): 


    path = r"C:\Users\PC\Downloads\ScreenRecording_06-08-2025_14-07-25_1.mov"
    capture = cv2.VideoCapture(path) # tehcnically an array of numpyndarray (frames)
    print(path)
    frame_array, sliding_window_size = video_frame_parser(capture)

    threshold = 16

    flicker_counter(frame_array, sliding_window_size, threshold)

if __name__ == '__main__':
    print(4)
    main()