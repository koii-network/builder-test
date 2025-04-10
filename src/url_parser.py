from urllib.parse import urlparse, parse_qs
from typing import Dict, Any, Optional

def parse_url(url: str) -> Dict[str, Any]:
    """
    Parse a given URL into its components.

    Args:
        url (str): The URL to parse.

    Returns:
        Dict[str, Any]: A dictionary containing parsed URL components.

    Raises:
        ValueError: If the input URL is invalid or empty.
    """
    # Check for empty or None input
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: URL must be a non-empty string")

    try:
        # Use urlparse to break down the URL
        parsed = urlparse(url)

        # Extract query parameters using parse_qs
        query_params = parse_qs(parsed.query)
        # Flatten single-item lists to their values
        query_params = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}

        # Construct and return the parsed URL dictionary
        return {
            'scheme': parsed.scheme or '',  # Change to empty string if None
            'netloc': parsed.netloc or '',  # Change to empty string if None
            'path': parsed.path or '',      # Change to empty string if None
            'params': parsed.params or None,
            'query': query_params,
            'fragment': parsed.fragment or '',  # Change to empty string if None
            'username': parsed.username,
            'password': parsed.password,
            'hostname': parsed.hostname,
            'port': parsed.port
        }
    except Exception as e:
        # Catch any unexpected parsing errors
        raise ValueError(f"Error parsing URL: {str(e)}")