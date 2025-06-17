
from helper_functions import luminance
from collections import deque
import matplotlib.pyplot as plt

def flicker_counter(frame_array, sliding_window_size, threshold):
    """
    Given an array of frames determine the number of flickers/flashes based of the relative 
    luminance of each frames as well as video sections that could trigger photoelyptic seizures.

    Args:
        frame_array (list[np.ndarray]): An array-like object of np.ndarrays
            representing RGB video frames

    Returns:
        trigger_sections (list[tuple(int, int)]: An array-like object counting tuples of start and end times of 
        trigger sections

    TODO: Implement trigger_sections, implement video overview system
    """

    f = 0
    last_frame_luminance = -1
    flicker_count = 0
    flashes = 0
    flag = 0
    luminance_queue = deque()
    contrast_values = []
    flicker_values = []
    lp, rp = 0, 0
    trigger_sections = []

    start_frame = 0
    end_frame = 0

    for frame in frame_array:
        average_frame_colour = frame.mean(axis=(0,1))

        # define what a flicker or a flash is 

        relative_luminance = luminance(average_frame_colour)

        # given relative_luminance, we compare with the last frame to determine if there was a flicker at the current frame. This is if contrast is above 3:1 threshold. 

        # case if we have max sliding window size
        
        
        if rp - lp >= sliding_window_size:
            contrast_ratio = (max(relative_luminance, last_frame_luminance) + 0.05) / (min(relative_luminance, last_frame_luminance) + 0.05)
    

            if (contrast_ratio >= 3.0):
                flicker_count += 1
                if flicker_count >= threshold and flag == 0:
                    flashes += 1
                    flag = 1
                    start_frame = f

            last_frame_luminance = relative_luminance
            luminance_queue.append(relative_luminance)
            rp += 1

            contrast_values.append(contrast_ratio)

            # check if the removed item forms a flicker 

            removed_luminance = luminance_queue.popleft()

            contrast_ratio = (max(removed_luminance, luminance_queue[0]) + 0.05) / (min(removed_luminance, luminance_queue[0]) + 0.05) # check to see if the removed item has a flicker with its neighbor

            if (contrast_ratio >= 3.0):
                flicker_count -= 1
                if flicker_count < threshold and flag == 1:
                    flag = 0
                    end_frame = f
                    trigger_sections.append((start_frame, end_frame))
            
            lp += 1
            

        # case if window size is not maxed out
        else: 
            if last_frame_luminance == -1: # this is the first frame analyzed so don't worry
                last_frame_luminance = relative_luminance
                luminance_queue.append(relative_luminance)
                rp += 1
                continue
            contrast_ratio = (max(relative_luminance, last_frame_luminance) + 0.05) / (min(relative_luminance, last_frame_luminance) + 0.05)


            if (contrast_ratio >= 3.0):
                flicker_count += 1
                if flicker_count >= threshold and flag == 0:
                    flashes += 1
                    flag = 1
                    start_frame = f
            contrast_values.append(contrast_ratio)
            last_frame_luminance = relative_luminance
            luminance_queue.append(relative_luminance)
            rp += 1
        f += 1
        flicker_values.append(flicker_count)
       
    x = [x for x in range(len(contrast_values))]
    plt.plot(x, contrast_values, label="contrast-values")
    plt.axhline(y=3, color='r', linestyle='-')
    plt.xlabel('Frame Number')
    plt.ylabel('Contrast Values')




    plt.title('Contrast values in Episode')

    # function to show the plot
    plt.show()

    plt.plot(x, flicker_values, label="flicker-values")
    plt.axhline(y=16, color='r', linestyle='-')
    plt.xlabel('Frame Number')
    plt.ylabel('Flicker Values within ' + str(sliding_window_size) + ' frame range')




    plt.title('Contrast values in Episode')

    # function to show the plot
    plt.show()
    return trigger_sections

    