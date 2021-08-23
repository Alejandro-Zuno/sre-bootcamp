import unittest
from methods import Token, Restricted
from werkzeug.exceptions import Forbidden

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.convert = Token()
        self.validate = Restricted()

    def test_generate_token(self):
        self.assertEqual('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoiYWRtaW4ifQ.m8UshTqghHSrbjd9O_xaHdQx-G4m4sz6JWCffMhvFtDTpCdqd30QKe-iFp0BjosWcL0htQnHhhi3qv_ec4zhew', self.convert.generate_token('admin'))

    def test_access_data(self):
        self.assertEqual('You are under protected data', self.validate.access_data('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoiYWRtaW4ifQ.m8UshTqghHSrbjd9O_xaHdQx-G4m4sz6JWCffMhvFtDTpCdqd30QKe-iFp0BjosWcL0htQnHhhi3qv_ec4zhew'))

    def test_access_data_wrong_token(self):
        self.assertEqual('Access Denied, Invalid Token', self.validate.access_data('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoiYWRaW4ifQ.m8UshTqghHSrbjd9O_xaHdQx-G4m4sz6JWCffMhvFtDTpCdqd30QKe-iFp0BjosWcL0htQnHhhi3qv_ec4zh'))

    def test_access_data_empty_token(self):
        self.assertEqual('Access Denied, Invalid Token', self.validate.access_data(''))

if __name__ == '__main__':
    unittest.main()
