from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
from methods import Token, Restricted
from authentication import userExists, passwordCheck

app = Flask(__name__)
login = Token()
protected = Restricted()


# Just a health check
@app.route("/")
def url_root():
    return "OK"


# Just a health check
@app.route("/_health")
def url_health():
    return "OK"


# e.g. http://127.0.0.1:8000/login
@app.route("/login", methods=['POST'])
def url_login():
    
    if not 'username' in request.form or not 'password' in request.form:
        abort(400, description="Missing Parameters")

    username = request.form['username']
    password = request.form['password']

    if not userExists(username):
        abort(403, description="Invalid Username or Password")

    role = passwordCheck(username,password)
    if not role:
        abort(403, description="Invalid Username or Password")

    res = {
        "data": login.generate_token(username)
    }

    return jsonify(res)


# # e.g. http://127.0.0.1:8000/protected
@app.route("/protected")
def url_protected():
    auth_token = request.headers.get('Authorization')

    if not 'Authorization' in request.headers:
        abort(403, description="Permission Denied, missing Authorization header")

    res = {
        "data": protected.access_data(auth_token)
    }
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
