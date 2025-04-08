from urllib.parse import urlparse, parse_qs

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
        
        # Flatten single-item query parameter lists
        query_params = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}
        
        # Construct and return a comprehensive dictionary of URL components
        return {
            'scheme': parsed.scheme,
            'netloc': parsed.netloc,
            'path': parsed.path,
            'params': parsed.params,
            'query': query_params,
            'fragment': parsed.fragment,
            'username': parsed.username,
            'password': parsed.password,
            'hostname': parsed.hostname,
            'port': parsed.port
        }
    except Exception as e:
        raise ValueError(f"Invalid URL: {str(e)}")