import pytest
from src.url_parser import parse_url

def test_parse_complete_url():
    url = 'https://www.example.com:8080/path/to/page?name=John&age=30#section'
    result = parse_url(url)
    assert result == {
        'protocol': 'https',
        'domain': 'www.example.com',
        'path': '/path/to/page',
        'query_params': {'name': ['John'], 'age': ['30']},
        'port': 8080,
        'fragment': 'section'
    }

def test_parse_simple_url():
    url = 'http://example.com'
    result = parse_url(url)
    assert result == {
        'protocol': 'http',
        'domain': 'example.com',
        'path': '/',
        'query_params': {},
        'port': None,
        'fragment': None
    }

def test_parse_url_with_query_params():
    url = 'https://example.com/search?q=python&lang=en'
    result = parse_url(url)
    assert result['query_params'] == {'q': ['python'], 'lang': ['en']}

def test_parse_url_with_no_protocol():
    url = 'example.com/path'
    result = parse_url(url)
    assert result == {
        'protocol': None,
        'domain': None,
        'path': 'example.com/path',
        'query_params': {},
        'port': None,
        'fragment': None
    }

def test_invalid_url_empty_string():
    with pytest.raises(ValueError, match="Invalid URL: URL must be a non-empty string"):
        parse_url('')

def test_invalid_url_none():
    with pytest.raises(ValueError, match="Invalid URL: URL must be a non-empty string"):
        parse_url(None)  # type: ignore

def test_url_with_special_characters():
    url = 'https://example.com/path?param=value%20with%20space'
    result = parse_url(url)
    assert result['query_params'] == {'param': ['value with space']}