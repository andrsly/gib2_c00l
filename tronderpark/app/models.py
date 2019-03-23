from app import db
#from werkzeug.security import generate_password_hash as gph, check_password_hash as cph


#class User(db.Model):
#    __tablename__ = 'user'
#    user_id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(64), unique=True )
#    email = db.Column(db.String(120), unique=True)
#    psw_hash = db.Column(db.String())
#    psw_repeat = db.Column(db.String(), unique=True) #men hva gjør egentlig unique?? hmm
     
#     def __repr__(self):
#        return '<User {}>'.format(self.username)   

#    def __init__(self, username, password):
#        self.username = username.lower()
#        self.pw_hash = gph(password)
    
#    def check_password(self, candidate):
#        return cph(self.pw_hash, candidate)
    
#class Parkhouse(db.Model):
#    __tablename__ = 'parkhouse'
#    park_id = db.Column(db.Integer, primary_key=True)
#    pname = db.Column(db.String(64), unique=True)
#    paddress = db.Column(db.String(128), unique=True)
#    popen = db.Column(db.String(), unique=True)

#class Relations(db.Model):
#    __tablename__ = 'relations'
#    comment_id = db.Column(db.Integer, primary_key=True)
#    pid = db.Column(db.Integer, ForeignKey('Parkhouse.park_id') 
#    uid = db.Column(db.Integer, ForeignKey('User.user_id')
#    comment = db.Column(db.String(256), unique=True)
#    user = relationship("User", backref=backref("user", uselist=False))
 