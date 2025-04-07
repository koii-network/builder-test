from urllib.parse import urlparse, parse_qs
from typing import Dict, Any, Optional

def parse_url(url: str) -> Dict[str, Any]:
    """
    Parse a given URL and extract its components.

    Args:
        url (str): The URL to parse.

    Returns:
        Dict[str, Any]: A dictionary containing parsed URL components:
        - protocol: URL protocol (e.g., 'http', 'https')
        - domain: Domain name
        - path: URL path
        - query_params: Dictionary of query parameters
        - port: Port number (if specified, otherwise None)
        - fragment: URL fragment (if any)

    Raises:
        ValueError: If the input URL is invalid or empty.
    """
    # Validate input
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: URL must be a non-empty string")

    try:
        # Parse the URL
        parsed_url = urlparse(url)

        # Extract components
        return {
            'protocol': parsed_url.scheme or None,
            'domain': parsed_url.hostname or None,
            'path': parsed_url.path or '/',
            'query_params': dict(parse_qs(parsed_url.query)) if parsed_url.query else {},
            'port': parsed_url.port,
            'fragment': parsed_url.fragment or None
        }
    except Exception as e:
        raise ValueError(f"Error parsing URL: {str(e)}")