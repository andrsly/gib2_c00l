from app import app
from flask import Flask, jsonify, render_template, redirect, url_for, request

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

@app.route ('/map/')
def map ():
    return render_template('map.html')

@app.route ('/work/')
def work():
    return render_template('work.html')

@app.route ('/review/')
def review ():
    return render_template('review.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Ugyldig brukernavn eller passord. Vennligst prøv igjen.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


if __name__ == "__main__":
   app.run(port=80,debug=True)
    
#@app.route('/register/')
#def register():
#    return render_template('register.html')
