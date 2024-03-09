from flask import Flask, request, jsonify, render_template, url_for, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = "lasdfoh389h9qhweohpqe8hgqh9hqwh49hq9hgq9h"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
db = SQLAlchemy(app)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = True


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




@app.route("/")
def index():
    #check if user already in session
    if "username" in session:
        if session["username"] == "admin":
            return redirect(url_for("admin"))
        else:
            return redirect(url_for("home"))
    else:
        return redirect(url_for("login"))



@app.route("/home")
def home():
    if "username" in session and session["username"] == "admin":
        return redirect(url_for("admin"))
    elif "username" in session and session["username"] != "admin":
        return redirect(url_for('records', user=session["username"]))
    else:
        flash("Unauthorized Access", "danger")
        return redirect(url_for("index"))
    


@app.route('/admin')
def admin():
    if "username" in session and session["username"] == "admin":
        users = Log.query.distinct().with_entities(Log.user).all()
        return render_template('admin_home.html', users=users)
    else:
        return redirect(url_for("login"))
    


@app.route("/login", methods=["POST", "GET"])
def login():
    if "username" in session:
        return redirect(url_for("index"))
    else:
        if request.method == "POST":
            found_user = User.query.filter_by(username=request.form["username"]).first()
            if found_user == None: 
                flash('User not found! Create an account.', 'info')
                return redirect(url_for("register"))
            elif found_user:
                if check_password_hash(found_user.password_hash, request.form["password"]):
                    session["username"] = found_user.username
                    session.permanent = True
                    return redirect(url_for("index"))
                else:
                    flash("Password incorrect!", "danger")
                    return redirect(url_for("login"))
        else:
            return render_template("login.html")
        


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        found_user = User.query.filter_by(username = request.form["username"]).first()
        #check if user already exist in database
        if found_user == None:
            if request.form["password"] == request.form["re-password"]:
                session["username"] = request.form["username"]
                session.permanent = True

                password_hash = generate_password_hash(request.form["password"])
                usr = User(session["username"], password_hash)
                db.session.add(usr)
                db.session.commit()

                flash("User registered!", "success")
                return redirect(url_for("index"))
            else:
                flash("Passwords not matching! Try again", "danger")
                return redirect(url_for("register"))
        else:
            flash("User already exists! Please login", "info")
            return redirect(url_for("login"))
    else:
        return render_template("register.html")



@app.route('/records/<user>')
def records(user):
    if "username" in session and session["username"] == "admin":
        records = Log.query.filter_by(user=user).all()
        return render_template('show_logs.html', user=user, logs=records)
    elif "username" in session and session["username"] == user:
        records = Log.query.filter_by(user=user).all()
        return render_template('show_logs.html', user=user, logs=records)
    else:
        flash("Unauthorized Access", "danger")
        return redirect(url_for("index"))
    


@app.route('/logs')
def logs():
    if "username" in session:
        if session["username"] == "admin":
            logs = Log.query.all()
            return render_template('show_logs.html', logs=logs)
        else:
            flash("Unauthorized Access", "danger")
            return redirect(url_for("home"))
    else:
        return redirect(url_for("login"))
    


@app.route('/insert', methods=['POST'])
def insert_data():
    logs = request.json
    for data in logs:
        log = Log(event=data['event'], time=data['time'], name=data['name'], suspected=data['suspected'], vid=data['vid'], pid=data['pid'], user=data['user'])
        db.session.add(log)
    db.session.commit()
    return jsonify({'message': 'Data inserted successfully'}), 200



@app.route("/logout")
def logout():
    if "username" in session:
        session.clear()
        flash('You have been logged out!', 'warning')
        return redirect(url_for("index"))
    else:
        session.clear()
        return redirect(url_for("index"))



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)

