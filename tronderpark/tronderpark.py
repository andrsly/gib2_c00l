from app import app, db
from app.models import user1, Carpark

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'user1': user1, 'Carpark': Carpark}