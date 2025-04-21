import pytest
from src.url_parser import parse_url

def test_full_url_parsing():
    """Test parsing a complete URL with all components"""
    url = "https://username:password@example.com:8080/path/to/page?key1=value1&key2=value2#fragment"
    result = parse_url(url)
    
    assert result["scheme"] == "https"
    assert result["netloc"] == "username:password@example.com:8080"
    assert result["path"] == "/path/to/page"
    assert result["query"] == {"key1": "value1", "key2": "value2"}
    assert result["fragment"] == "fragment"
    assert result["username"] == "username"
    assert result["password"] == "password"
    assert result["hostname"] == "example.com"
    assert result["port"] == 8080

def test_simple_url_parsing():
    """Test parsing a simple URL"""
    url = "http://www.example.com"
    result = parse_url(url)
    
    assert result["scheme"] == "http"
    assert result["netloc"] == "www.example.com"
    assert result["path"] == ""
    assert result["query"] == {}
    assert result["fragment"] == ""

def test_url_with_query_params():
    """Test URL with multiple query parameters"""
    url = "https://example.com/search?q=python&category=programming"
    result = parse_url(url)
    
    assert result["query"] == {"q": "python", "category": "programming"}

def test_url_with_multiple_same_query_params():
    """Test URL with multiple values for same query parameter"""
    url = "https://example.com/search?tag=python&tag=programming"
    result = parse_url(url)
    
    assert result["query"] == {"tag": ["python", "programming"]}

def test_empty_url_raises_error():
    """Test that empty URL raises a ValueError"""
    with pytest.raises(ValueError, match="URL must be a non-empty string"):
        parse_url("")

def test_none_url_raises_error():
    """Test that None input raises a ValueError"""
    with pytest.raises(ValueError, match="URL must be a non-empty string"):
        parse_url(None)

def test_invalid_url_parsing():
    """Test parsing an invalid URL"""
    with pytest.raises(ValueError, match="Invalid URL"):
        parse_url("not valid")

def test_url_with_no_scheme():
    """Test URL without a scheme"""
    url = "example.com/path"
    result = parse_url(url)
    
    assert result["scheme"] == ""
    assert result["netloc"] == ""
    assert result["path"] == "example.com/path"