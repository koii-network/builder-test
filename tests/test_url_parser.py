import pytest
from src.url_parser import parse_url

def test_parse_url_full_url():
    url = "https://username:password@example.com:8080/path/to/page?param1=value1&param2=value2#section"
    result = parse_url(url)
    
    assert result['scheme'] == 'https'
    assert result['netloc'] == 'username:password@example.com:8080'
    assert result['path'] == '/path/to/page'
    assert result['hostname'] == 'example.com'
    assert result['port'] == 8080
    assert result['username'] == 'username'
    assert result['password'] == 'password'
    assert result['query'] == {'param1': 'value1', 'param2': 'value2'}
    assert result['fragment'] == 'section'

def test_parse_url_minimal_url():
    url = "http://example.com"
    result = parse_url(url)
    
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'example.com'
    assert result['path'] == ''
    assert result['hostname'] == 'example.com'
    assert result['port'] is None
    assert result['username'] is None
    assert result['password'] is None
    assert result['query'] == {}
    assert result['fragment'] == ''

def test_parse_url_with_query_params():
    url = "https://example.com/search?q=python&category=programming"
    result = parse_url(url)
    
    assert result['query'] == {'q': 'python', 'category': 'programming'}

def test_parse_url_error_handling():
    with pytest.raises(ValueError, match="URL must be a non-empty string"):
        parse_url("")
    
    with pytest.raises(ValueError, match="URL must be a non-empty string"):
        parse_url(None)

def test_parse_url_with_multiple_same_query_params():
    url = "https://example.com/page?tag=python&tag=programming"
    result = parse_url(url)
    
    assert result['query'] == {'tag': ['python', 'programming']}

def test_parse_url_with_special_characters():
    url = "https://example.com/path?special=hello%20world&unicode=こんにちは"
    result = parse_url(url)
    
    assert result['query'] == {'special': 'hello world', 'unicode': 'こんにちは'}