def rgb_to_hex(r: int, g: int, b: int) -> str:
    """
    Convert RGB color values to a hexadecimal color code.

    Args:
        r (int): Red color value (0-255)
        g (int): Green color value (0-255)
        b (int): Blue color value (0-255)

    Returns:
        str: Hexadecimal color code representing the RGB values

    Raises:
        ValueError: If any color value is outside the range 0-255
    """
    # Validate input values
    for color, name in [(r, 'Red'), (g, 'Green'), (b, 'Blue')]:
        if not isinstance(color, int):
            raise TypeError(f"{name} value must be an integer")
        if color < 0 or color > 255:
            raise ValueError(f"{name} value must be between 0 and 255")
    
    # Convert each color value to a two-digit hex representation
    hex_color = '#{:02X}{:02X}{:02X}'.format(r, g, b)
    
    return hex_color