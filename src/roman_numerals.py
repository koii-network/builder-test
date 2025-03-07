def int_to_roman(number: int) -> str:
    """
    Convert a non-negative integer (0-3999) to its Roman numeral representation.

    Args:
        number (int): An integer between 0 and 3999 (inclusive).

    Returns:
        str: The Roman numeral representation of the input number.

    Raises:
        ValueError: If the input is not in the range 0-3999.
    """
    # Validate input range
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    if number < 0 or number > 3999:
        raise ValueError("Input must be between 0 and 3999")

    # Special case for zero
    if number == 0:
        return "N"  # Using 'N' to represent zero, as classical Roman numerals had no zero

    # Define Roman numeral mappings
    roman_map = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    # Convert number to Roman numeral
    result = ""
    for value, symbol in roman_map:
        while number >= value:
            result += symbol
            number -= value

    return result