from app import db, login, app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy(app)

class user1(UserMixin, db.Model):
    ___tablename__ = "user1"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, username, email, password):
        self.username = username.title()
        self.email = email.lower()
        self.set_password(password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<user1 {}>'.format(self.username)

@login.user_loader
def load_user(id):
    return user1.query.get(int(id))

class Carpark(db.Model):
    __tablename__ = "Carpark"
    park_id = db.Column(db.Integer, primary_key=True)
    p_name = db.Column(db.String(64), index=True, unique=True)
    p_open = db.Column(db.String(36), index=True)
    p_close = db.Column(db.String(36), index=True)
    p_price = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<Carpark {}>'.format(self.body)