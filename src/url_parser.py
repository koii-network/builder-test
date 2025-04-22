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
        raise ValueError("URL must be a non-empty string")
    
    try:
        # Use urlparse to break down the URL
        parsed = urlparse(url)
        
        # Extract query parameters
        query_params = parse_qs(parsed.query)
        
        # Flatten single-item lists in query parameters
        query_params = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}
        
        # Construct the result dictionary
        result = {
            'scheme': parsed.scheme,
            'netloc': parsed.netloc,
            'path': parsed.path,
            'params': parsed.params,
            'query': query_params,
            'fragment': parsed.fragment,
            
            # Additional helpful components
            'hostname': parsed.hostname,
            'port': parsed.port,
            'username': parsed.username,
            'password': parsed.password
        }
        
        return result
    
    except Exception as e:
        raise ValueError(f"Invalid URL: {str(e)}")