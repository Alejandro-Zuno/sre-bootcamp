import unittest
from methods import Token, Restricted
from werkzeug.exceptions import Forbidden

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.convert = Token()
        self.validate = Restricted()

    def test_generate_token(self):
        self.assertEqual('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4ifQ.BmcZ8aB5j8wLSK8CqdDwkGxZfFwM1X1gfAIN7cXOx9w', self.convert.generate_token('admin'))

    def test_access_data(self):
        self.assertEqual('You are under protected data', self.validate.access_data('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4ifQ.BmcZ8aB5j8wLSK8CqdDwkGxZfFwM1X1gfAIN7cXOx9w'))

    def test_access_data_wrong_token(self):
        self.assertEqual('Access Denied, Invalid Token', self.validate.access_data('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4ifQ.BmcZ8aB5j8wLSK8qdDwkGxZfFwM1X1gfAIN7cXOx9w'))

    def test_access_data_empty_token(self):
        self.assertEqual('Access Denied, Invalid Token', self.validate.access_data(''))

if __name__ == '__main__':
    unittest.main()
