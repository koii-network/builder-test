import pytest
from src.url_parser import parse_url

def test_parse_complete_url():
    """Test parsing a complete URL with all components."""
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

def test_parse_simple_url():
    """Test parsing a simple URL."""
    url = "http://www.example.com"
    result = parse_url(url)
    
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'www.example.com'
    assert result['path'] == ''
    assert result['query'] == {}
    assert result['fragment'] == ''
    assert result['hostname'] == 'www.example.com'
    assert result['port'] is None

def test_parse_url_with_query_params():
    """Test parsing a URL with multiple query parameters."""
    url = "https://example.com/search?q=python&category=programming"
    result = parse_url(url)
    
    assert result['query'] == {'q': 'python', 'category': 'programming'}

def test_parse_url_with_empty_components():
    """Test parsing a URL with some empty components."""
    url = "https://example.com/"
    result = parse_url(url)
    
    assert result['scheme'] == 'https'
    assert result['netloc'] == 'example.com'
    assert result['path'] == '/'
    assert result['query'] == {}

def test_invalid_url_input():
    """Test error handling for invalid URL inputs."""
    with pytest.raises(ValueError, match="Invalid URL"):
        parse_url("")
    
    with pytest.raises(ValueError, match="Invalid URL"):
        parse_url(None)

def test_malformed_url():
    """Test parsing a malformed URL."""
    url = "not a valid url"
    result = parse_url(url)
    
    assert result['scheme'] == ''
    assert result['netloc'] == ''