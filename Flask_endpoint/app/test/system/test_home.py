from  unittest import TestCase
from Flask_endpoint.app.app import app
import  json

class TestHome(TestCase):
    def test_home(self):
        with app.test_client() as c:
            resp = c.get('/') # Testing home endpoint

            self.assertEqual(resp.status_code, 200)  # Testing status code
            self.assertEqual(json.loads(resp.get_data()), {'message': 'Hello World'})  # Getting json data
