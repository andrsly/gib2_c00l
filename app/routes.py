from app import app
from flask import jsonify

@app.route('/')
def helloworld():
    return jsonify(dict(data='Hello World'))

@app.route('/user/<username>')
def user(username):
    return jsonify(dict(user=username))
