from urllib.parse import urlparse, parse_qs
from typing import Dict, Any


def parse_url(url: str) -> Dict[str, Any]:
    """
    Parse a given URL into its components.

    Args:
        url (str): The URL to parse.

    Returns:
        Dict[str, Any]: A dictionary containing parsed URL components.

    Raises:
        ValueError: If the URL is invalid or empty.
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

        # Handle credentials, host, and port
        if '@' in parsed_url.netloc:
            # Split credentials and host
            credentials, host_port = parsed_url.netloc.split('@')
            
            # Parse credentials
            if ':' in credentials:
                username, password = credentials.split(':')
                result['username'] = username
                result['password'] = password
            else:
                result['username'] = credentials
                result['password'] = None
        else:
            host_port = parsed_url.netloc
            result['username'] = None
            result['password'] = None

        # Handle host and port
        if ':' in host_port:
            host, port = host_port.split(':')
            result['host'] = host
            result['port'] = port
        else:
            result['host'] = host_port
            result['port'] = None

        return result

    except Exception as e:
        raise ValueError(f"Error parsing URL: {str(e)}")