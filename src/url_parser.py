from urllib.parse import urlparse, unquote
from typing import Dict, Any, Optional, Union, List

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
        query_params: Dict[str, Union[str, List[str]]] = {}
        if parsed_url.query:
            # Use custom parsing to handle multiple parameters
            for param in parsed_url.query.split('&'):
                if '=' in param:
                    key, value = param.split('=', 1)
                    decoded_key = unquote(key)
                    
                    # Handle multiple values for the same key
                    if decoded_key in query_params:
                        if isinstance(query_params[decoded_key], list):
                            query_params[decoded_key].append(value)  # type: ignore
                        else:
                            query_params[decoded_key] = [query_params[decoded_key], value]  # type: ignore
                    else:
                        query_params[decoded_key] = value
        
        # Construct and return the parsed URL dictionary
        return {
            'scheme': parsed_url.scheme or None,
            'netloc': parsed_url.netloc or None,
            'path': parsed_url.path or None,
            'params': parsed_url.params or None,
            'query': query_params,
            'fragment': parsed_url.fragment or None,
            'username': parsed_url.username,
            'password': parsed_url.password,
            'hostname': parsed_url.hostname,
            'port': parsed_url.port
        }
    except Exception as e:
        # Catch any unexpected parsing errors
        raise ValueError(f"Error parsing URL: {str(e)}")