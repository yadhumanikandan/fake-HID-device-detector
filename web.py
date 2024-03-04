from flask import Flask, request, jsonify, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    age = db.Column(db.Integer)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/users')
def display_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'name': user.name, 'email': user.email, 'age': user.age} for user in users]
    return jsonify({'users': user_list}), 200

@app.route('/insert', methods=['POST'])
def insert_data():
    data = request.json
    user = User(name=data['name'], email=data['email'], age=data['age'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'Data inserted successfully'}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)