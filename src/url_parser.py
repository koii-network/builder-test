from urllib.parse import urlparse
from typing import Dict, Any, Optional
import re

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
    
    # Add more strict URL validation
    url_regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https:// or ftp:// or ftps://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    if not url_regex.match(url):
        raise ValueError(f"Invalid URL format: {url}")
    
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
        raise ValueError(f"Invalid URL format: {url}")