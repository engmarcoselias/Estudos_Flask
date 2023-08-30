from app import app, db


class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email