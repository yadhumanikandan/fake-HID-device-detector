from config import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)

    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(400))
    time = db.Column(db.String(100))
    name = db.Column(db.String(100))
    suspected = db.Column(db.Boolean)
    vid = db.Column(db.String(10))
    pid = db.Column(db.String(10))
    user = db.Column(db.String(50))