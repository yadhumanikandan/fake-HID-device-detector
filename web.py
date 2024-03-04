from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@hostname/database_name'
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     email = db.Column(db.String(100))
#     age = db.Column(db.Integer)

@app.route('/insert', methods=['POST'])
def insert_data():
    data = request.json
    print(data['name'], data['email'], data['age'])
    # db.session.add(user)
    # db.session.commit()
    return jsonify({'message': 'Data inserted successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)