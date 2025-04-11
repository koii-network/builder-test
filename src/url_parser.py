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
        # Parse URL, potentially treating it as a path if no parsing occurs
        parsed = urlparse(url)
        
        # If parsing fails or seems incorrect, try alternative parsing
        if not parsed.netloc:
            # For URLs like "example.com/path" or "example.com"
            if '/' in url:
                # Split first occurrence of /
                parts = url.split('/', 1)
                parsed = parsed._replace(netloc=parts[0], path='/' + parts[1] if len(parts) > 1 else '')
            else:
                # Assume whole URL is netloc
                parsed = parsed._replace(netloc=url, path='')
        
        # Extract query parameters
        query_params = parse_qs(parsed.query)
        
        # Flatten single-item lists in query params
        query_params = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}
        
        # Construct and return the parsed URL dictionary
        return {
            'scheme': parsed.scheme or '',
            'netloc': '' if not parsed.netloc else parsed.netloc,
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