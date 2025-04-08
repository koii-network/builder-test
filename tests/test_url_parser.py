import pytest
from src.url_parser import parse_url

def test_full_url_parsing():
    """Test parsing a full URL with all components."""
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
    """Test parsing a minimal URL."""
    url = "http://example.com"
    result = parse_url(url)
    
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'example.com'
    assert result['path'] == ''
    assert result['query'] == {}
    assert result['fragment'] == ''
    assert result['hostname'] == 'example.com'
    assert result['port'] is None

def test_url_with_query_params():
    """Test URL with multiple query parameters."""
    url = "https://example.com/search?q=python&lang=en"
    result = parse_url(url)
    
    assert result['query'] == {'q': 'python', 'lang': 'en'}

def test_url_with_multiple_same_params():
    """Test URL with multiple values for same parameter."""
    url = "https://example.com/search?tag=python&tag=programming"
    result = parse_url(url)
    
    assert result['query'] == {'tag': ['python', 'programming']}

def test_empty_url_raises_error():
    """Test that empty URL raises a ValueError."""
    with pytest.raises(ValueError, match="URL must be a non-empty string"):
        parse_url("")

def test_none_url_raises_error():
    """Test that None input raises a ValueError."""
    with pytest.raises(ValueError, match="URL must be a non-empty string"):
        parse_url(None)

def test_invalid_url_raises_error():
    """Test that an invalid URL raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid URL"):
        parse_url("not a valid url")

def test_ipv6_url():
    """Test parsing a URL with an IPv6 address."""
    url = "https://[2001:0db8:85a3:0000:0000:8a2e:0370:7334]:8080/path"
    result = parse_url(url)
    
    assert result['scheme'] == 'https'
    assert result['hostname'] == '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
    assert result['port'] == 8080
    assert result['path'] == '/path'