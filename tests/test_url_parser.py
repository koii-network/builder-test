import pytest
from src.url_parser import parse_url

def test_full_url_parsing():
    """Test parsing a complete URL with all components"""
    url = "https://www.example.com:8080/path/to/page?param1=value1&param2=value2#section"
    result = parse_url(url)
    
    assert result == {
        'protocol': 'https',
        'domain': 'www.example.com',
        'path': '/path/to/page',
        'query_params': {'param1': 'value1', 'param2': 'value2'},
        'port': 8080,
        'fragment': 'section'
    }

def test_url_without_port():
    """Test parsing a URL without a port"""
    url = "http://github.com/user/repo"
    result = parse_url(url)
    
    assert result == {
        'protocol': 'http',
        'domain': 'github.com',
        'path': '/user/repo',
        'query_params': {},
        'port': None,
        'fragment': None
    }

def test_url_with_complex_query_params():
    """Test parsing URL with multiple values for same parameter"""
    url = "https://example.com/search?tag=python&tag=programming"
    result = parse_url(url)
    
    assert result == {
        'protocol': 'https',
        'domain': 'example.com',
        'path': '/search',
        'query_params': {'tag': ['python', 'programming']},
        'port': None,
        'fragment': None
    }

def test_url_with_fragment():
    """Test parsing URL with fragment"""
    url = "https://docs.python.org/3/library/urllib.parse.html#urlparse"
    result = parse_url(url)
    
    assert result == {
        'protocol': 'https',
        'domain': 'docs.python.org',
        'path': '/3/library/urllib.parse.html',
        'query_params': {},
        'port': None,
        'fragment': 'urlparse'
    }

def test_empty_url_raises_error():
    """Test that empty URL raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid URL: URL must be a non-empty string"):
        parse_url("")

def test_none_url_raises_error():
    """Test that None input raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid URL: URL must be a non-empty string"):
        parse_url(None)

def test_invalid_url_handling():
    """Test handling of an invalid URL"""
    with pytest.raises(ValueError, match="Error parsing URL"):
        parse_url("not a valid url")