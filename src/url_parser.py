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
    if not url or not isinstance(url, str):
        raise ValueError("URL must be a non-empty string")
    
    # Basic validation to check for truly invalid URLs
    if not any(char in url for char in ['/', '.']):
        raise ValueError("Invalid URL")
    
    try:
        # Use urlparse to break down the URL
        parsed = urlparse(url)
        
        # Extract query parameters
        query_params = parse_qs(parsed.query)
        
        # Convert query parameters from lists to single values if possible
        cleaned_params = {}
        for key, value in query_params.items():
            cleaned_params[key] = value[0] if len(value) == 1 else value
        
        # Normalize empty strings and None values
        scheme = parsed.scheme or ""
        netloc = parsed.netloc or ""
        path = parsed.path or ""
        fragment = parsed.fragment or ""
        
        # Construct and return the parsed URL dictionary
        return {
            "scheme": scheme,
            "netloc": netloc,
            "path": path,
            "params": parsed.params or None,
            "query": cleaned_params,
            "fragment": fragment,
            "username": parsed.username,
            "password": parsed.password,
            "hostname": parsed.hostname,
            "port": parsed.port
        }
    except Exception as e:
        # For other unexpected errors
        raise ValueError(f"Invalid URL: {str(e)}")