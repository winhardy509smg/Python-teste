from flask_testing import TestCase
from app import app

class AppTestCase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello World", response.data)

if __name__ == "__main__":
    import unittest
    unittest.main()
