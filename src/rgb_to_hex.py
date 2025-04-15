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
        ValueError: If any color value is outside the range 0-255
    """
    # Validate input values
    if not all(isinstance(val, int) for val in (r, g, b)):
        raise TypeError("RGB values must be integers")
    
    if not all(0 <= val <= 255 for val in (r, g, b)):
        raise ValueError("RGB values must be between 0 and 255")
    
    # Convert each color component to a two-digit hex value
    hex_color = '#{:02X}{:02X}{:02X}'.format(r, g, b)
    
    return hex_color