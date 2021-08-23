# These functions need to be implemented
import jwt 
import os
from authentication import tokenVerification, getRole
from flask import abort

class Token:

    def generate_token(self,user):
        encoded_jwt = jwt.encode({"role": getRole(user)}, os.environ['JWT_SEED'], algorithm="HS512")
        return encoded_jwt


class Restricted:

    def access_data(self, authorization):
        token = str.replace(str(authorization), 'Bearer ', '')
        if tokenVerification(token):
            return "You are under protected data"
        else:
            return "Access Denied, Invalid Token"
