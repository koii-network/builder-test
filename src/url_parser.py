from urllib.parse import urlparse
from typing import Dict, Any, Optional

def parse_url(url: str) -> Dict[str, Optional[str]]:
    """
    Parse a given URL into its components.
    
    Args:
        url (str): The URL to parse.
    
    Returns:
        Dict[str, Optional[str]]: A dictionary containing URL components.
    
    Raises:
        ValueError: If the input is not a valid URL.
    """
    # Validate input
    if not isinstance(url, str):
        raise ValueError("Input must be a string")
    
    if not url.strip():
        raise ValueError("URL cannot be empty")
    
    try:
        # Use urlparse to break down the URL
        parsed_url = urlparse(url)
        
        # Return a comprehensive dictionary of URL components
        return {
            'scheme': parsed_url.scheme or None,
            'netloc': parsed_url.netloc or None,
            'path': parsed_url.path or None,
            'params': parsed_url.params or '',  # Change to empty string instead of None
            'query': parsed_url.query or None,
            'fragment': parsed_url.fragment or None,
            'username': parsed_url.username or None,
            'password': parsed_url.password or None,
            'hostname': parsed_url.hostname or None,
            'port': parsed_url.port or None
        }
    except Exception:
        # Check for basic URL format
        if '.' not in url or not url.startswith(('http://', 'https://', 'ftp://')):
            raise ValueError(f"Invalid URL format: {url}")
        raise