import pytest
from src.url_parser import parse_url

def test_basic_url_parsing():
    """Test parsing a basic URL"""
    url = "https://www.example.com/path/to/page"
    result = parse_url(url)
    assert result['scheme'] == 'https'
    assert result['hostname'] == 'www.example.com'
    assert result['path'] == '/path/to/page'

def test_url_with_query_params():
    """Test parsing URL with query parameters"""
    url = "https://example.com/search?q=python&category=programming"
    result = parse_url(url)
    assert result['scheme'] == 'https'
    assert result['query'] == {'q': ['python'], 'category': ['programming']}

def test_url_with_port():
    """Test parsing URL with port number"""
    url = "http://localhost:8080/api"
    result = parse_url(url)
    assert result['scheme'] == 'http'
    assert result['hostname'] == 'localhost'
    assert result['port'] == '8080'
    assert result['path'] == '/api'

def test_url_with_credentials():
    """Test parsing URL with username and password"""
    url = "https://username:password@example.com/private"
    result = parse_url(url)
    assert result['username'] == 'username'
    assert result['password'] == 'password'
    assert result['hostname'] == 'example.com'
    assert result['path'] == '/private'

def test_url_with_fragment():
    """Test parsing URL with fragment"""
    url = "https://docs.example.com/page#section1"
    result = parse_url(url)
    assert result['fragment'] == 'section1'

def test_invalid_url_empty():
    """Test handling of empty URL"""
    with pytest.raises(ValueError, match="Invalid URL"):
        parse_url("")

def test_invalid_url_none():
    """Test handling of None input"""
    with pytest.raises(ValueError, match="Invalid URL"):
        parse_url(None)

def test_complex_url():
    """Test parsing a complex URL with multiple components"""
    url = "https://user:pass@example.com:8443/path/to/resource?key1=value1&key2=value2#fragment"
    result = parse_url(url)
    assert result['scheme'] == 'https'
    assert result['username'] == 'user'
    assert result['password'] == 'pass'
    assert result['hostname'] == 'example.com'
    assert result['port'] == '8443'
    assert result['path'] == '/path/to/resource'
    assert result['query'] == {'key1': ['value1'], 'key2': ['value2']}
    assert result['fragment'] == 'fragment'