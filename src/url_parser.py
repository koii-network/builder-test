from urllib.parse import urlparse, parse_qs, unquote

def parse_url(url):
    """
    Parse a given URL into its component parts.
    
    Args:
        url (str): The URL to parse
    
    Returns:
        dict: A dictionary containing parsed URL components
    
    Raises:
        ValueError: If the URL is invalid or empty
    """
    # Check for empty or None input
    if not url or not isinstance(url, str):
        raise ValueError("URL must be a non-empty string")
    
    try:
        # Use urlparse to break down the URL
        parsed = urlparse(url)
        
        # Parse query parameters 
        query_params = parse_qs(parsed.query)
        
        # Flatten single-item query parameter lists and decode values
        query_params = {
            unquote(k): unquote(v[0]) if len(v) == 1 else [unquote(val) for val in v] 
            for k, v in query_params.items()
        }
        
        # Construct and return a comprehensive dictionary of URL components
        return {
            'scheme': parsed.scheme,
            'netloc': parsed.netloc,
            'path': unquote(parsed.path),  # Decode path
            'params': parsed.params,
            'query': query_params,
            'fragment': parsed.fragment,
            'username': unquote(parsed.username) if parsed.username else None,
            'password': unquote(parsed.password) if parsed.password else None,
            'hostname': parsed.hostname,
            'port': parsed.port
        }
    except Exception as e:
        raise ValueError(f"Invalid URL: {str(e)}")