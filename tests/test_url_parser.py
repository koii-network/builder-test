import pytest
from src.url_parser import parse_url

def test_full_url():
    """Test parsing a complete URL with all components."""
    url = "https://username:password@example.com:8080/path/to/page?query=value#fragment"
    result = parse_url(url)
    
    assert result == {
        'scheme': 'https',
        'netloc': 'username:password@example.com:8080',
        'path': '/path/to/page',
        'params': '',
        'query': 'query=value',
        'fragment': 'fragment',
        'username': 'username',
        'password': 'password',
        'hostname': 'example.com',
        'port': 8080
    }

def test_minimal_url():
    """Test parsing a minimal URL."""
    url = "https://example.com"
    result = parse_url(url)
    
    assert result['scheme'] == 'https'
    assert result['netloc'] == 'example.com'
    assert result['path'] is None
    assert result['query'] is None
    assert result['fragment'] is None

def test_url_with_path():
    """Test URL with path."""
    url = "http://example.com/path/to/resource"
    result = parse_url(url)
    
    assert result['scheme'] == 'http'
    assert result['path'] == '/path/to/resource'

def test_url_with_query():
    """Test URL with query parameters."""
    url = "https://example.com/search?q=python&category=programming"
    result = parse_url(url)
    
    assert result['query'] == 'q=python&category=programming'

def test_url_with_fragment():
    """Test URL with fragment."""
    url = "https://example.com/page#section"
    result = parse_url(url)
    
    assert result['fragment'] == 'section'

def test_invalid_input_type():
    """Test that non-string input raises a ValueError."""
    with pytest.raises(ValueError, match="Input must be a string"):
        parse_url(123)

def test_empty_url():
    """Test that empty URL raises a ValueError."""
    with pytest.raises(ValueError, match="URL cannot be empty"):
        parse_url("")
    with pytest.raises(ValueError, match="URL cannot be empty"):
        parse_url("   ")

def test_invalid_url():
    """Test that malformed URL raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid URL format"):
        parse_url("not a valid url")