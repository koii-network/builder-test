from urllib.parse import urlparse, parse_qs
from typing import Dict, Any

def parse_url(url: str) -> Dict[str, Any]:
    """
    Parse a given URL into its component parts.

    Args:
        url (str): The URL to be parsed.

    Returns:
        Dict[str, Any]: A dictionary containing parsed URL components:
        - protocol: The URL scheme (e.g., 'http', 'https')
        - domain: The domain name
        - port: The port number (or None if not specified)
        - path: The path component of the URL
        - query_params: A dictionary of query parameters
        - fragment: The fragment identifier (or None if not present)

    Raises:
        ValueError: If the input is not a valid URL string.
    """
    # Validate input
    if not isinstance(url, str):
        raise ValueError("Input must be a string")
    
    # Handle empty or whitespace-only strings
    if not url.strip():
        raise ValueError("URL cannot be empty")

    try:
        # Use urlparse to break down the URL
        parsed_url = urlparse(url)
        
        # Extract query parameters
        query_params = parse_qs(parsed_url.query)
        # Convert query params to their single values if possible
        query_params = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}

        # Construct the result dictionary
        return {
            'protocol': parsed_url.scheme or None,
            'domain': parsed_url.hostname or None,
            'port': parsed_url.port,
            'path': parsed_url.path or None,
            'query_params': query_params,
            'fragment': parsed_url.fragment or None
        }
    except Exception:
        raise ValueError(f"Invalid URL: {url}")