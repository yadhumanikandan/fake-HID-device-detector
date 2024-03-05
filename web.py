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

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(400))
    time = db.Column(db.String(100))
    name = db.Column(db.String(100))
    suspected = db.Column(db.Boolean)
    vid = db.Column(db.String(10))
    pid = db.Column(db.String(10))


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/users')
def display_users():
    logs = Log.query.all()
    log_list = [{'id': log.id, 'event': log.event, 'time': log.time, 'name': log.name, 'suspected': log.suspected, 'vid': log.vid, 'pid': log.pid} for log in logs]
    return jsonify({'logs': log_list}), 200

@app.route('/insert', methods=['POST'])
def insert_data():
    logs = request.json


    for data in logs:
        log = Log(event=data['event'], time=data['time'], name=data['name'], suspected=data['suspected'], vid=data['vid'], pid=data['pid'])
        db.session.add(log)
    db.session.commit()
    return jsonify({'message': 'Data inserted successfully'}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)

