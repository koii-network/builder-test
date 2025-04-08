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

        # Additional parsing for netloc
        if '@' in parsed_url.netloc:
            # Split credentials if present
            credentials, host = parsed_url.netloc.split('@')
            if ':' in credentials:
                username, password = credentials.split(':')
                result['username'] = username
                result['password'] = password
            else:
                result['username'] = credentials
        
        # Handle host and port
        if ':' in parsed_url.netloc:
            host_parts = parsed_url.netloc.split(':')
            result['host'] = host_parts[0]
            result['port'] = host_parts[1] if len(host_parts) > 1 else None
        else:
            result['host'] = parsed_url.netloc
            result['port'] = None

        return result

    except Exception as e:
        raise ValueError(f"Error parsing URL: {str(e)}")