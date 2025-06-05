
def luminance(colorarray):
    """Calculates the relative luminance of an RGB color.

    The input should be a list or tuple containing three integers representing
    the red, green, and blue components of a color in the standard RGB color
    space (0–255 range). These definitions are in accordance with the WCAG standards available at
    https://www.w3.org/WAI/GL/wiki/Relative_luminance#New_Methodology_for_WCAG_3. 

    Args:
        colorarray (list[int] or tuple[int, int, int]): An array-like object of length 3
            representing RGB color components.

    Returns:
        np.float64: The relative luminance value of the color.
    """
    
    colorarray = colorarray/255 
    
    luminance_array = list(map(lambda x: x/12.92 if x <= 0.04045 else ((x+0.055)/1.055) ** 2.4 ,colorarray))
   
    relative_luminance = 0.2126 * luminance_array[0] + 0.7152 * luminance_array[1] + 0.0722 * luminance_array[2]

    return relative_luminance