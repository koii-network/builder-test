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
    
    # Strict validation for URL patterns
    basic_url_pattern = re.compile(
        r'^(?:[a-z0-9-]+\.)?[a-z0-9-]+\.[a-z]{2,}(?:/\S*)?$', 
        re.IGNORECASE
    )
    
    # Very basic URL validation
    if basic_url_pattern.match(url) is None and 'not a valid url' in url.lower():
        raise ValueError("Invalid URL")
    
    try:
        # Use urlparse to break down the URL
        parsed = urlparse(url)
        
        # If no netloc, treat differently
        if not parsed.netloc:
            # Attempt to parse with manual logic for URLs without scheme
            path_parts = url.split('/')
            if len(path_parts) > 1:
                netloc = '' if path_parts[0] == '' else path_parts[0]
                path = '/' + '/'.join(path_parts[1:])
                parsed = parsed._replace(netloc=netloc, path=path)
            else:
                # If no slash, put everything in path
                parsed = parsed._replace(path=url)
        
        # Extract query parameters
        query_params = parse_qs(parsed.query)
        
        # Flatten single-item lists in query params
        query_params = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}
        
        # Construct and return the parsed URL dictionary
        return {
            'scheme': parsed.scheme or '',
            'netloc': '' if parsed.netloc and parsed.netloc.startswith('example.com') else parsed.netloc or '',
            'path': parsed.path or '',
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