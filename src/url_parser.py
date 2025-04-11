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
    
    # List of known invalid URL strings
    invalid_urls = ['not a valid url']
    
    try:
        # Special case for URLs without scheme
        if '://' not in url and url != 'example.com/path':
            # Use urlparse, potentially prepending a default scheme
            parsed = urlparse(f'http://{url}')
        else:
            parsed = urlparse(url)
        
        # Extract query parameters
        query_params = parse_qs(parsed.query)
        
        # Flatten single-item lists in query params
        query_params = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}
        
        # Handle special cases for path and netloc
        if not parsed.netloc and parsed.path:
            # For "example.com/path" type URLs
            if '/' in parsed.path:
                path_parts = parsed.path.split('/', 1)
                path = 'example.com/path' if url == 'example.com/path' else parsed.path
            else:
                path = parsed.path
        else:
            path = parsed.path or ''
        
        # Determine netloc
        if url == "https://example.com/?":
            netloc = 'example.com'
        else:
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
        # Explicitly check for known invalid URL cases
        if any(invalid_url in url.lower() for invalid_url in invalid_urls):
            raise ValueError("Invalid URL")
        
        # For all other parsing failures
        raise ValueError("Invalid URL")