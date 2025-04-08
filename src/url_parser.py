from urllib.parse import urlparse, parse_qs
from typing import Dict, Any

def parse_url(url: str) -> Dict[str, Any]:
    """
    Parse a given URL into its component parts.
    
    Args:
        url (str): The URL to parse.
    
    Returns:
        Dict[str, Any]: A dictionary containing parsed URL components.
    
    Raises:
        ValueError: If the URL is invalid or empty.
    """
    # Check for empty or None input
    if not url or not isinstance(url, str):
        raise ValueError("URL must be a non-empty string")
    
    try:
        # Use urlparse to break down the URL
        parsed_url = urlparse(url)
        
        # Additional validation for invalid URLs
        if not parsed_url.scheme or not parsed_url.netloc:
            raise ValueError(f"Invalid URL: {url}")
        
        # Extract query parameters
        query_params = parse_qs(parsed_url.query)
        
        # Flatten single-item lists in query parameters
        query_params = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}
        
        # Construct and return the parsed URL dictionary
        return {
            'scheme': parsed_url.scheme,
            'netloc': parsed_url.netloc,
            'path': parsed_url.path,
            'params': parsed_url.params,
            'query': query_params,
            'fragment': parsed_url.fragment,
            'username': parsed_url.username,
            'password': parsed_url.password,
            'hostname': parsed_url.hostname,
            'port': parsed_url.port
        }
    except ValueError:
        raise
    except Exception:
        # Catch any unexpected parsing errors
        raise ValueError(f"Invalid URL: {url}")