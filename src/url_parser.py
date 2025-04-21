from urllib.parse import urlparse, parse_qs
from typing import Dict, Any, Optional

def parse_url(url: str) -> Dict[str, Any]:
    """
    Parse a given URL into its components.
    
    Args:
        url (str): The URL to parse.
    
    Returns:
        Dict[str, Any]: A dictionary containing URL components:
        - scheme: The URL scheme (protocol)
        - netloc: The network location (domain)
        - path: The path component of the URL
        - params: The query parameters as a dictionary
        - fragment: The fragment identifier
    
    Raises:
        ValueError: If the input URL is empty or invalid
    """
    # Check for empty or None input
    if not url:
        raise ValueError("URL cannot be empty")
    
    try:
        # Use urlparse to break down the URL
        parsed_url = urlparse(url)
        
        # Parse query parameters
        query_params = parse_qs(parsed_url.query)
        
        # Convert single-item lists to their values for cleaner output
        query_params = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}
        
        # Construct and return the parsed URL dictionary
        return {
            'scheme': parsed_url.scheme,
            'netloc': parsed_url.netloc,
            'path': parsed_url.path,
            'params': query_params,
            'fragment': parsed_url.fragment
        }
    except Exception as e:
        raise ValueError(f"Invalid URL: {str(e)}")