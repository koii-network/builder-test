import pytest
from src.url_parser import parse_url

def test_basic_url_parsing():
    url = "https://www.example.com/path?key1=value1&key2=value2#fragment"
    result = parse_url(url)
    
    assert result['scheme'] == 'https'
    assert result['netloc'] == 'www.example.com'
    assert result['path'] == '/path'
    assert result['query'] == {'key1': 'value1', 'key2': 'value2'}
    assert result['fragment'] == 'fragment'

def test_url_with_authentication():
    url = "https://username:password@www.example.com:8080/path"
    result = parse_url(url)
    
    assert result['username'] == 'username'
    assert result['password'] == 'password'
    assert result['hostname'] == 'www.example.com'
    assert result['port'] == 8080

def test_url_with_multiple_query_values():
    url = "http://example.com/path?key=value1&key=value2"
    result = parse_url(url)
    
    assert result['query'] == {'key': ['value1', 'value2']}

def test_invalid_url_raises_error():
    with pytest.raises(ValueError, match="URL must be a non-empty string"):
        parse_url(None)
    
    with pytest.raises(ValueError, match="URL must be a non-empty string"):
        parse_url("")

def test_minimal_url():
    url = "http://example.com"
    result = parse_url(url)
    
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'example.com'
    assert result['path'] == ''
    assert result['query'] == {}
    assert result['fragment'] == ''

def test_url_with_special_characters():
    url = "https://example.com/path%20with%20spaces?key=value%20with%20space"
    result = parse_url(url)
    
    assert result['path'] == '/path with spaces'
    assert result['query'] == {'key': 'value with space'}