import pytest
from src.url_parser import parse_url

def test_full_url_parsing():
    """Test parsing a full URL with all components"""
    url = "https://www.example.com/path/to/page?param1=value1&param2=value2#section"
    result = parse_url(url)
    
    assert result == {
        'scheme': 'https',
        'netloc': 'www.example.com',
        'path': '/path/to/page',
        'params': {
            'param1': 'value1', 
            'param2': 'value2'
        },
        'fragment': 'section'
    }

def test_url_with_multiple_params():
    """Test URL with multiple values for same parameter"""
    url = "http://example.com/search?tag=python&tag=programming"
    result = parse_url(url)
    
    assert result == {
        'scheme': 'http',
        'netloc': 'example.com',
        'path': '/search',
        'params': {
            'tag': ['python', 'programming']
        },
        'fragment': ''
    }

def test_minimal_url():
    """Test parsing a minimal URL"""
    url = "https://example.com"
    result = parse_url(url)
    
    assert result == {
        'scheme': 'https',
        'netloc': 'example.com',
        'path': '',
        'params': {},
        'fragment': ''
    }

def test_url_with_no_scheme():
    """Test URL without a scheme"""
    url = "example.com/path"
    result = parse_url(url)
    
    assert result == {
        'scheme': '',
        'netloc': '',
        'path': 'example.com/path',
        'params': {},
        'fragment': ''
    }

def test_empty_url_raises_error():
    """Test that empty URL raises a ValueError"""
    with pytest.raises(ValueError, match="URL cannot be empty"):
        parse_url("")

def test_none_url_raises_error():
    """Test that None input raises a ValueError"""
    with pytest.raises(ValueError, match="URL cannot be empty"):
        parse_url(None)  # type: ignore

def test_complex_url_with_special_characters():
    """Test URL with special characters and encoding"""
    url = "https://example.com/search?q=hello%20world&lang=en"
    result = parse_url(url)
    
    assert result == {
        'scheme': 'https',
        'netloc': 'example.com',
        'path': '/search',
        'params': {
            'q': 'hello world', 
            'lang': 'en'
        },
        'fragment': ''
    }