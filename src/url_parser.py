from urllib.parse import urlparse, parse_qs
from typing import Dict, Any, Optional

def parse_url(url: str) -> Dict[str, Any]:
    """
    Parse a given URL into its components.
    
    Args:
        url (str): The URL to parse
    
    Returns:
        Dict[str, Any]: A dictionary containing parsed URL components
    
    Raises:
        ValueError: If the URL is invalid or empty
    """
    # Check for empty or None input
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: URL must be a non-empty string")
    
    try:
        # Use urlparse to break down the URL
        parsed_url = urlparse(url)
        
        # Extract query parameters
        query_params = parse_qs(parsed_url.query)
        
        # Flatten single-item lists in query params
        query_params = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}
        
        # Construct the result dictionary
        return {
            "scheme": parsed_url.scheme or None,
            "netloc": parsed_url.netloc or None,
            "path": parsed_url.path or None,
            "params": parsed_url.params or None,
            "query": query_params,
            "fragment": parsed_url.fragment or None,
            "username": parsed_url.username,
            "password": parsed_url.password,
            "hostname": parsed_url.hostname,
            "port": parsed_url.port
        }
    except Exception as e:
        raise ValueError(f"Error parsing URL: {str(e)}")