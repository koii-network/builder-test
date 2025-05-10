def rgb_to_hex(r: int, g: int, b: int) -> str:
    """
    Convert RGB color values to a hexadecimal color representation.

    Args:
        r (int): Red color value (0-255)
        g (int): Green color value (0-255)
        b (int): Blue color value (0-255)

    Returns:
        str: Hexadecimal color representation (uppercase)

    Raises:
        ValueError: If any RGB value is not in the range 0-255
    """
    # Validate input values
    for color, name in [(r, 'Red'), (g, 'Green'), (b, 'Blue')]:
        if not isinstance(color, int):
            raise TypeError(f"{name} value must be an integer")
        if color < 0 or color > 255:
            raise ValueError(f"{name} value must be between 0 and 255")
    
    # Convert to hex and ensure two-digit representation
    hex_color = '#{:02X}{:02X}{:02X}'.format(r, g, b)
    return hex_color