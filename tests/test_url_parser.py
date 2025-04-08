import pytest
from src.url_parser import parse_url


def test_basic_url():
    """Test parsing a basic URL."""
    url = "https://www.example.com/path/to/page"
    result = parse_url(url)
    assert result['scheme'] == 'https'
    assert result['host'] == 'www.example.com'
    assert result['path'] == '/path/to/page'


def test_url_with_query_params():
    """Test parsing a URL with query parameters."""
    url = "https://example.com/search?q=python&lang=en"
    result = parse_url(url)
    assert result['query'] == {'q': ['python'], 'lang': ['en']}


def test_url_with_port():
    """Test parsing a URL with a port."""
    url = "http://localhost:8080/api"
    result = parse_url(url)
    assert result['scheme'] == 'http'
    assert result['host'] == 'localhost'
    assert result['port'] == '8080'
    assert result['path'] == '/api'


def test_url_with_credentials():
    """Test parsing a URL with username and password."""
    url = "https://username:password@example.com/path"
    result = parse_url(url)
    assert result['username'] == 'username'
    assert result['password'] == 'password'
    assert result['host'] == 'example.com'


def test_url_with_fragment():
    """Test parsing a URL with a fragment."""
    url = "https://example.com/page#section"
    result = parse_url(url)
    assert result['fragment'] == 'section'


def test_invalid_url_empty():
    """Test parsing an empty URL."""
    with pytest.raises(ValueError, match="Invalid URL: URL must be a non-empty string"):
        parse_url("")


def test_invalid_url_none():
    """Test parsing None input."""
    with pytest.raises(ValueError, match="Invalid URL: URL must be a non-empty string"):
        parse_url(None)


def test_complex_url():
    """Test parsing a complex URL with multiple components."""
    url = "https://user:pass@example.com:8443/path/to/resource?key1=value1&key2=value2#fragment"
    result = parse_url(url)
    assert result['scheme'] == 'https'
    assert result['username'] == 'user'
    assert result['password'] == 'pass'
    assert result['host'] == 'example.com'
    assert result['port'] == '8443'
    assert result['path'] == '/path/to/resource'
    assert result['query'] == {'key1': ['value1'], 'key2': ['value2']}
    assert result['fragment'] == 'fragment'