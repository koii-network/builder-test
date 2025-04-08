import pytest
from src.url_parser import parse_url

def test_full_url_parsing():
    """Test parsing a complete URL with all components"""
    url = "https://username:password@example.com:8080/path/to/page?param1=value1&param2=value2#fragment"
    result = parse_url(url)
    
    assert result['scheme'] == 'https'
    assert result['netloc'] == 'username:password@example.com:8080'
    assert result['path'] == '/path/to/page'
    assert result['query'] == {'param1': 'value1', 'param2': 'value2'}
    assert result['fragment'] == 'fragment'
    assert result['username'] == 'username'
    assert result['password'] == 'password'
    assert result['hostname'] == 'example.com'
    assert result['port'] == 8080

def test_minimal_url():
    """Test parsing a minimal URL"""
    url = "http://example.com"
    result = parse_url(url)
    
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'example.com'
    assert result['path'] is None
    assert result['query'] == {}
    assert result['fragment'] is None

def test_url_with_query_params():
    """Test URL with multiple query parameters"""
    url = "https://example.com/search?q=python&category=programming"
    result = parse_url(url)
    
    assert result['query'] == {'q': 'python', 'category': 'programming'}

def test_url_with_special_characters():
    """Test URL with encoded and special characters"""
    url = "https://example.com/path?param=value%20with%20spaces"
    result = parse_url(url)
    
    assert result['query'] == {'param': 'value with spaces'}

def test_invalid_url_raises_error():
    """Test that invalid URLs raise a ValueError"""
    with pytest.raises(ValueError, match="Invalid URL"):
        parse_url("")
    
    with pytest.raises(ValueError, match="Invalid URL"):
        parse_url(None)

def test_url_with_no_scheme():
    """Test URL without a scheme"""
    url = "example.com/path"
    result = parse_url(url)
    
    assert result['scheme'] is None
    assert result['path'] == 'example.com/path'

def test_ipv6_url():
    """Test URL with IPv6 address"""
    url = "https://[2001:db8::1]/path"
    result = parse_url(url)
    
    assert result['scheme'] == 'https'
    assert result['hostname'] == '[2001:db8::1]'
    assert result['path'] == '/path'

def test_url_with_multiple_query_values():
    """Test URL with query parameter having multiple values"""
    url = "https://example.com/search?tag=python&tag=programming"
    result = parse_url(url)
    
    assert result['query'] == {'tag': ['python', 'programming']}