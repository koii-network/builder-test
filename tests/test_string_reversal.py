import unittest
import json
from app import create_app

class TestStringReversal(unittest.TestCase):
    def setUp(self):
        """
        Set up test client for making requests
        """
        self.app = create_app()
        self.client = self.app.test_client()
    
    def test_reverse_string_success(self):
        """
        Test successful string reversal
        """
        response = self.client.post(
            '/api/reverse', 
            data=json.dumps({'string': 'hello'}),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['reversed_string'], 'olleh')
    
    def test_reverse_empty_string(self):
        """
        Test reversing an empty string
        """
        response = self.client.post(
            '/api/reverse', 
            data=json.dumps({'string': ''}),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['reversed_string'], '')
    
    def test_reverse_with_spaces(self):
        """
        Test reversing a string with spaces
        """
        response = self.client.post(
            '/api/reverse', 
            data=json.dumps({'string': 'hello world'}),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['reversed_string'], 'dlrow olleh')
    
    def test_missing_string_parameter(self):
        """
        Test error handling when no string is provided
        """
        response = self.client.post(
            '/api/reverse', 
            data=json.dumps({}),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()