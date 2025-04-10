from urllib.parse import urlparse, parse_qs, unquote
from typing import Dict, Any, Optional

def parse_url(url: str) -> Dict[str, Any]:
    """
    Parse a given URL into its component parts.
    
    Args:
        url (str): The URL to parse
    
    Returns:
        Dict[str, Any]: A dictionary containing URL components
    
    Raises:
        ValueError: If the URL is invalid or empty
    """
    # Check for empty or None input
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: URL must be a non-empty string")
    
    try:
        # Parse the URL
        parsed_url = urlparse(url)
        
        # Extract query parameters with raw URL-encoded values
        query_params = {}
        if parsed_url.query:
            # Use custom parsing to preserve URL-encoded values
            for param in parsed_url.query.split('&'):
                if '=' in param:
                    key, value = param.split('=', 1)
                    query_params[unquote(key)] = value
        
        # Flatten multiple instances of the same parameter into a list
        combined_params = {}
        for key, value in query_params.items():
            if key in combined_params:
                if isinstance(combined_params[key], list):
                    combined_params[key].append(value)
                else:
                    combined_params[key] = [combined_params[key], value]
            else:
                combined_params[key] = value
        
        # Construct and return the parsed URL dictionary
        return {
            'scheme': parsed_url.scheme or None,
            'netloc': parsed_url.netloc or None,
            'path': parsed_url.path or None,
            'params': parsed_url.params or None,
            'query': combined_params,
            'fragment': parsed_url.fragment or None,
            'username': parsed_url.username,
            'password': parsed_url.password,
            'hostname': parsed_url.hostname,
            'port': parsed_url.port
        }
    except Exception as e:
        # Catch any unexpected parsing errors
        raise ValueError(f"Error parsing URL: {str(e)}")