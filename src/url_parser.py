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
        raise ValueError("Invalid URL: URL must be a non-empty string")
    
    try:
        # Use urlparse to break down the URL
        parsed_url = urlparse(url)
        
        # Prepare the result dictionary
        result = {
            'scheme': parsed_url.scheme,
            'netloc': parsed_url.netloc,
            'path': parsed_url.path,
            'params': parsed_url.params,
            'query': parse_qs(parsed_url.query),
            'fragment': parsed_url.fragment
        }
        
        # Extract additional useful information
        # Split netloc into username, password, hostname, and port
        if '@' in parsed_url.netloc:
            # Handle credentials
            credentials, host = parsed_url.netloc.split('@', 1)
            if ':' in credentials:
                result['username'], result['password'] = credentials.split(':', 1)
            else:
                result['username'] = credentials
        
        # Split host and port
        if ':' in parsed_url.netloc:
            hostname_port = parsed_url.netloc.split(':')
            result['hostname'] = hostname_port[0]
            if len(hostname_port) > 1:
                result['port'] = hostname_port[1]
        else:
            result['hostname'] = parsed_url.netloc
        
        return result
    
    except Exception as e:
        raise ValueError(f"Error parsing URL: {str(e)}")