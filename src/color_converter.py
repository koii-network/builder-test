def rgb_to_hex(r, g, b):
    """
    Convert RGB color values to a hexadecimal color code.

    Args:
        r (int or float): Red color value (0-255)
        g (int or float): Green color value (0-255)
        b (int or float): Blue color value (0-255)

    Returns:
        str: Hexadecimal color code (e.g., '#FF0000' for red)

    Raises:
        ValueError: If any color value is outside the valid range of 0-255
        TypeError: If color values are not numeric
    """
    # Validate input types
    if not all(isinstance(x, (int, float)) for x in (r, g, b)):
        raise TypeError("RGB values must be numeric")
    
    # Convert to integers and validate range
    try:
        r = int(r)
        g = int(g)
        b = int(b)
    except ValueError:
        raise TypeError("RGB values must be convertible to integers")

    # Check color value ranges
    if not all(0 <= x <= 255 for x in (r, g, b)):
        raise ValueError("RGB values must be between 0 and 255")

    # Convert to hex, ensuring two-digit representation
    return f'#{r:02X}{g:02X}{b:02X}'