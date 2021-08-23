from database import mydb
import hashlib
import jwt 
from jwt.exceptions import ExpiredSignatureError,InvalidSignatureError,DecodeError
import os

def userExists(username):
    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT username FROM users WHERE username=%(username)s', { 'username' : username })
    checkUsername = my_cursor.fetchone()

    if checkUsername is None:
        return False
    else:
        return True

def passwordCheck(username, password):
    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT password,salt,role FROM users WHERE username=%(username)s', { 'username' : username })
    pass_salt_role = my_cursor.fetchone()
    
    hashedPass=pass_salt_role[0]
    saltedPass=password+pass_salt_role[1]
    role=pass_salt_role[2]
    hashedInput = hashlib.sha512(saltedPass.encode('utf-8')).hexdigest()
    if hashedInput == hashedPass:
        return role
    else:
        return False

def getRole(username):
    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT role FROM users WHERE username=%(username)s', { 'username' : username })
    role = my_cursor.fetchone()
    return role[0]


def tokenVerification(token):
    try:
        jwt.decode(token, os.environ['JWT_SEED'], algorithms=['HS256'])
        return True
    except ExpiredSignatureError:
        return False
    except InvalidSignatureError:
        return False
    except DecodeError:
        return False