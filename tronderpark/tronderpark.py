from app import app, db
from app.models import User1, Carpark

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User1': User1, 'Carpark': Carpark}