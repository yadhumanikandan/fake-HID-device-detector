from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.secret_key = "lasdfoh389h9qhweohpqe8hgqh9hqwh49hq9hgq9h"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
db = SQLAlchemy(app)
app.debug = True

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = True