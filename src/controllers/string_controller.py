from src.utils.string_utils import reverse_string

class StringController:
    @staticmethod
    def reverse(input_string: str) -> str:
        """
        Controller method to reverse a string.
        
        Args:
            input_string (str): The string to be reversed
        
        Returns:
            str: The reversed string
        """
        return reverse_string(input_string)