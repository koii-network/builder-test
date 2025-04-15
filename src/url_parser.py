from urllib.parse import urlparse, parse_qs
from typing import Dict, Any, Optional

def parse_url(url: str) -> Dict[str, Any]:
    """
    Parse a URL into its components and return a dictionary with detailed information.

    Args:
        url (str): The URL to parse.

    Returns:
        Dict[str, Any]: A dictionary containing parsed URL components:
        - protocol: The URL protocol (http, https, etc.)
        - domain: The domain name
        - path: The path component of the URL
        - query_params: A dictionary of query parameters
        - port: The port number (if specified, otherwise None)
        - fragment: The fragment identifier (if present, otherwise None)

    Raises:
        ValueError: If the input URL is invalid or empty.
    """
    # Check for empty or None input
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: URL must be a non-empty string")

    try:
        # Try to parse the URL, raising an error if it fails
        parsed = urlparse(url)
        
        # Require a scheme (protocol) to be a valid URL
        if not parsed.scheme:
            raise ValueError("Invalid URL: Missing protocol")

        # Require a netloc (domain) to be a valid URL
        if not parsed.netloc:
            raise ValueError("Invalid URL: Missing domain")

        # Extract query parameters
        query_params = parse_qs(parsed.query)
        # Convert query params from lists to single values if possible
        query_params = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}

        # Construct the result dictionary
        return {
            'protocol': parsed.scheme,
            'domain': parsed.netloc.split(':')[0],  # Remove port if present
            'path': parsed.path,
            'query_params': query_params,
            'port': parsed.port,
            'fragment': parsed.fragment or None
        }
    except Exception as e:
        raise ValueError(f"Error parsing URL: {str(e)}")