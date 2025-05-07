def rgb_to_hex(*args):
    """
    Convert RGB color values to a hexadecimal color code.
    
    Args:
        *args: Either 3 individual integer values (r, g, b) 
               or a single tuple/list of 3 RGB values
    
    Returns:
        str: Hexadecimal color code (e.g., '#FF0000' for bright red)
    
    Raises:
        ValueError: If RGB values are not in the range 0-255 
                    or incorrect number of arguments is provided
    """
    # Handle different input formats
    if len(args) == 1 and isinstance(args[0], (tuple, list)):
        rgb = args[0]
    elif len(args) == 3:
        rgb = args
    else:
        raise ValueError("Input must be either 3 separate values or a single tuple/list of 3 values")
    
    # Validate input
    if len(rgb) != 3:
        raise ValueError("Exactly 3 color values (R, G, B) are required")
    
    # Check each value is in valid range
    for color in rgb:
        if not isinstance(color, int):
            raise ValueError("RGB values must be integers")
        if color < 0 or color > 255:
            raise ValueError("RGB values must be between 0 and 255")
    
    # Convert to hexadecimal
    return '#{:02X}{:02X}{:02X}'.format(rgb[0], rgb[1], rgb[2])