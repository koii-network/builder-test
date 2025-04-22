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
        # Validate basic structure of the URL
        if not any(char in url for char in ['/', '.', ':']):
            raise ValueError(f"Invalid URL: {url}")

        # Try parsing with potential manual protocol handling
        if '://' not in url:
            # If the URL contains path, treat it as a potential http URL
            if '/' in url:
                # If there's a path, try http:// 
                parsed_url = urlparse('http://' + url)
                protocol = None
            else:
                # If just a domain, try http://
                parsed_url = urlparse('http://' + url)
                protocol = None
        else:
            # If protocol is present, use as-is
            parsed_url = urlparse(url)
            protocol = parsed_url.scheme
        
        # Extract query parameters
        query_params = parse_qs(parsed_url.query)
        # Convert query params to their single values if possible
        query_params = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}

        # Determine path
        path = parsed_url.path if parsed_url.path and parsed_url.path != '/' else None

        # Ensure path starts with '/' if present
        if path and not path.startswith('/'):
            path = '/' + path

        # Construct the result dictionary
        return {
            'protocol': protocol,
            'domain': parsed_url.hostname,
            'port': parsed_url.port,
            'path': path,
            'query_params': query_params,
            'fragment': parsed_url.fragment or None
        }
    except Exception:
        raise ValueError(f"Invalid URL: {url}")