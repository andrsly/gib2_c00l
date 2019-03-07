from app import app
from flask import Flask, jsonify, render_template

#@app.route('/')
#def helloworld():
#    return jsonify(dict(data='Hello World'))

#@app.route('/user/<username>')
#def user(username):
#    return jsonify(dict(user=username))

@app.route ('/templates/nettsiden.html')
def nettsiden ():
    return render_template('nettsiden.html')

@app.route ('/')
def home ():
    return render_template('home.html')