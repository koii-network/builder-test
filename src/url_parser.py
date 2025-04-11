from urllib.parse import urlparse, parse_qs
from typing import Dict, Any, Optional
import re

def parse_url(url: str) -> Dict[str, Any]:
    """
    Parse a given URL into its component parts.
    
    Args:
        url (str): The URL to parse
    
    Returns:
        Dict[str, Any]: A dictionary containing parsed URL components
    
    Raises:
        ValueError: If the URL is invalid or empty
    """
    # Check for empty or None input
    if not url:
        raise ValueError("URL cannot be empty")
    
    # Basic URL validation regex
    url_pattern = re.compile(
        r'^(?:(?:https?|ftp)://)?'  # optional scheme
        r'(?:(?:[a-z0-9-]+\.)+[a-z]{2,})'  # domain
        r'(?:/[^\s]*)?$',  # optional path
        re.IGNORECASE
    )
    
    # Check for very basic URL structure
    if not url_pattern.match(url):
        raise ValueError("Invalid URL")
    
    try:
        # Use urlparse to break down the URL
        # Special handling for URLs without a scheme
        if '://' not in url:
            # Prepend temporary scheme for parsing, but keep scheme empty
            parsed = urlparse('temp://' + url)
            parsed = parsed._replace(scheme='')
        else:
            parsed = urlparse(url)
        
        # Extract query parameters
        query_params = parse_qs(parsed.query)
        
        # Flatten single-item lists in query params
        query_params = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}
        
        # Handle path and special cases
        path = parsed.path or ''
        netloc = parsed.netloc or ''
        
        # Construct and return the parsed URL dictionary
        return {
            'scheme': parsed.scheme or '',
            'netloc': netloc,
            'path': path,
            'params': parsed.params or None,
            'query': query_params,
            'fragment': parsed.fragment or None,
            'username': parsed.username,
            'password': parsed.password,
            'hostname': parsed.hostname,
            'port': parsed.port
        }
    except Exception:
        raise ValueError("Invalid URL")