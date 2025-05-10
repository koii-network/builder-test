import pytest
from src.url_parser import parse_url

def test_parse_complete_url():
    url = "https://username:password@example.com:8080/path/to/page?key1=value1&key2=value2#fragment"
    result = parse_url(url)
    
    assert result['scheme'] == 'https'
    assert result['netloc'] == 'username:password@example.com:8080'
    assert result['path'] == '/path/to/page'
    assert result['query'] == {'key1': 'value1', 'key2': 'value2'}
    assert result['fragment'] == 'fragment'
    assert result['username'] == 'username'
    assert result['password'] == 'password'
    assert result['hostname'] == 'example.com'
    assert result['port'] == 8080

def test_parse_simple_url():
    url = "http://www.example.com"
    result = parse_url(url)
    
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'www.example.com'
    assert result['path'] == ''
    assert result['query'] == {}
    assert result['fragment'] is None

def test_parse_url_with_multiple_query_params():
    url = "https://example.com/search?category=books&price=10-50"
    result = parse_url(url)
    
    assert result['query'] == {'category': 'books', 'price': '10-50'}

def test_parse_url_with_empty_components():
    url = "https://example.com/?"
    result = parse_url(url)
    
    assert result['scheme'] == 'https'
    assert result['netloc'] == 'example.com'
    assert result['path'] == '/'
    assert result['query'] == {}

def test_empty_url_raises_error():
    with pytest.raises(ValueError, match="URL cannot be empty"):
        parse_url("")

def test_invalid_url_raises_error():
    with pytest.raises(ValueError, match="Invalid URL"):
        parse_url("not a valid url")

def test_url_without_scheme():
    url = "example.com/path"
    result = parse_url(url)
    
    assert result['scheme'] == ''
    assert result['netloc'] == ''
    assert result['path'] == 'example.com/path'