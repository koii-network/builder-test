import pytest
from src.url_parser import parse_url

def test_full_url_parsing():
    url = "https://username:password@example.com:8080/path/to/page?key1=value1&key2=value2#fragment"
    parsed = parse_url(url)
    
    assert parsed['scheme'] == 'https'
    assert parsed['netloc'] == 'username:password@example.com:8080'
    assert parsed['path'] == '/path/to/page'
    assert parsed['query'] == {'key1': 'value1', 'key2': 'value2'}
    assert parsed['fragment'] == 'fragment'
    assert parsed['username'] == 'username'
    assert parsed['password'] == 'password'
    assert parsed['hostname'] == 'example.com'
    assert parsed['port'] == 8080

def test_minimal_url():
    url = "http://example.com"
    parsed = parse_url(url)
    
    assert parsed['scheme'] == 'http'
    assert parsed['netloc'] == 'example.com'
    assert parsed['path'] is None
    assert parsed['query'] == {}
    assert parsed['fragment'] is None

def test_url_with_query_params():
    url = "https://example.com/search?q=python&category=programming"
    parsed = parse_url(url)
    
    assert parsed['query'] == {'q': 'python', 'category': 'programming'}

def test_url_with_multiple_same_query_params():
    url = "https://example.com/page?tag=python&tag=programming"
    parsed = parse_url(url)
    
    assert parsed['query'] == {'tag': ['python', 'programming']}

def test_invalid_url_input():
    with pytest.raises(ValueError, match="Invalid URL"):
        parse_url("")
    
    with pytest.raises(ValueError, match="Invalid URL"):
        parse_url(None)

def test_url_without_scheme():
    url = "example.com/path"
    parsed = parse_url(url)
    
    assert parsed['scheme'] is None
    assert parsed['netloc'] is None
    assert parsed['path'] == 'example.com/path'

def test_url_with_special_characters():
    url = "https://example.com/path%20with%20spaces?key=value%20with%20spaces"
    parsed = parse_url(url)
    
    assert parsed['path'] == '/path%20with%20spaces'
    assert parsed['query'] == {'key': 'value%20with%20spaces'}