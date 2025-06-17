import cv2

def play_video_segment(capture, start_frame, end_frame, wait=30, window_name='Video Segment'):
    """
    Plays a video segment between start_frame and end_frame using an OpenCV VideoCapture object.

    Args:
        capture (cv2.VideoCapture): OpenCV VideoCapture object.
        start_frame (int): Index of the first frame to play.
        end_frame (int): Index of the last frame to play.
        wait (int): Delay in milliseconds between frames (default 30 ms).
        window_name (str): Name of the display window.
    """
    if not capture.isOpened():
        print("Error: VideoCapture is not opened.")
        return

    total_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

    if start_frame < 0 or end_frame >= total_frames or start_frame > end_frame:
        print("Error: Invalid start or end frame.")
        return

    capture.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    current_frame = start_frame
    while current_frame <= end_frame:
        ret, frame = capture.read()
        if not ret:
            print("Error reading frame.")
            break

        cv2.imshow(window_name, frame)
        key = cv2.waitKey(wait)
        if key == ord('q'):
            break

        current_frame += 1

    
    cv2.destroyAllWindows()
