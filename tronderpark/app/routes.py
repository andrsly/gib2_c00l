from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user #logout_user
from app.models import User1

@app.route('/')
def home():
    return render_template('/home.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    #if current_user.is_authenticated:
    #    return redirect('/home/')
    form = LoginForm()
    if form.validate_on_submit():
        user = User1.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/login')
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('.home'))
    print('hei')
    return render_template('/login.html', title='Logg inn', form=form)

#@app.route('/logout/')
#def logout():
#    logout_user()
#    return redirect(url_for('.index'))

@app.route('/register/', methods=['GET', 'POST'])
def register():
#   if current_user.is_authenticated:
#        return redirect('/index')
    print('hei2')
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User1(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('.login'))
    return render_template('register.html', title='Register', form=form)

@app.route ('/templates/nettsiden.html')
def nettsiden ():
    return render_template('nettsiden.html')

@app.route ('/map/')
def map ():
    return render_template('map.html')

@app.route ('/work/')
def work():
    return render_template('work.html')

@app.route ('/review/')
def review ():
    return render_template('review.html')