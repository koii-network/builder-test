from urllib.parse import urlparse, parse_qs
from typing import Dict, Any, Optional

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
    
    try:
        # Use urlparse to break down the URL
        # Add default scheme if not present to help with parsing
        if '://' not in url:
            url = 'http://' + url
        
        parsed = urlparse(url)
        
        # Extract query parameters
        query_params = parse_qs(parsed.query)
        
        # Flatten single-item lists in query params
        query_params = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}
        
        # Handle path and scheme to match test expectations
        path = parsed.path or ''
        scheme = parsed.scheme or ''
        
        # Special handling for URLs without a clear scheme/netloc
        if not parsed.netloc and '://' not in url:
            netloc = ''
            path = url
        else:
            netloc = parsed.netloc or ''
        
        # Construct and return the parsed URL dictionary
        return {
            'scheme': scheme,
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
    except Exception as e:
        raise ValueError("Invalid URL")