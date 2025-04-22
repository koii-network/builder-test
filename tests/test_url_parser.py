import pytest
from src.url_parser import parse_url

def test_complete_url():
    """Test parsing a complete URL with all components."""
    url = "https://www.example.com:8080/path/to/page?key1=value1&key2=value2#section"
    result = parse_url(url)
    
    assert result == {
        'protocol': 'https',
        'domain': 'www.example.com',
        'port': 8080,
        'path': '/path/to/page',
        'query_params': {'key1': 'value1', 'key2': 'value2'},
        'fragment': 'section'
    }

def test_minimal_url():
    """Test parsing a minimal URL with just protocol and domain."""
    url = "http://example.com"
    result = parse_url(url)
    
    assert result == {
        'protocol': 'http',
        'domain': 'example.com',
        'port': None,
        'path': None,
        'query_params': {},
        'fragment': None
    }

def test_url_with_multiple_query_params():
    """Test URL with multiple query parameters."""
    url = "https://example.com/search?q=test&category=books&sort=relevance"
    result = parse_url(url)
    
    assert result == {
        'protocol': 'https',
        'domain': 'example.com',
        'port': None,
        'path': '/search',
        'query_params': {
            'q': 'test', 
            'category': 'books', 
            'sort': 'relevance'
        },
        'fragment': None
    }

def test_url_with_no_protocol():
    """Test URL without a protocol."""
    url = "example.com/path"
    result = parse_url(url)
    
    assert result == {
        'protocol': None,
        'domain': 'example.com',
        'port': None,
        'path': '/path',
        'query_params': {},
        'fragment': None
    }

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(ValueError, match="Input must be a string"):
        parse_url(123)
    
    with pytest.raises(ValueError, match="Input must be a string"):
        parse_url(None)

def test_empty_string():
    """Test error handling for empty or whitespace-only strings."""
    with pytest.raises(ValueError, match="URL cannot be empty"):
        parse_url("")
    
    with pytest.raises(ValueError, match="URL cannot be empty"):
        parse_url("   ")

def test_invalid_url():
    """Test error handling for clearly invalid URLs."""
    with pytest.raises(ValueError, match="Invalid URL"):
        parse_url("not a valid url")