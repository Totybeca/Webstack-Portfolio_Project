import os
from flask import Flask, render_template, request, url_for, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = "WEzQn9a3Um"

Session(app)

db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True, nullable=False)
  fullname = db.Column(db.String(), nullable=False)
  phone = db.Column(db.String(), nullable=False)
  email = db.Column(db.String(), nullable=False)
  password = db.Column(db.String(), nullable=False)

class Contact(db.Model):
  id = db.Column(db.Integer, primary_key=True, nullable=False)
  name = db.Column(db.String(), nullable=False)
  phone = db.Column(db.String(), nullable=False)
  email = db.Column(db.String(), nullable=False)
  message = db.Column(db.String(), nullable=False)  

with app.app_context():
  db.create_all()

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/pay')
def pay():
  return render_template('pay.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/contact', methods = ['POST'])
def contact_form_submit():
  contact = Contact()
  contact.name = request.form['name']
  contact.phone = request.form['phone']
  contact.email = request.form['email']
  contact.message = request.form['message']

  db.session.add(contact)
  db.session.commit()
  flash('Your message was successfully sent')
  return redirect(url_for('contact'))  

@app.route('/register', methods = ['GET'])
def show_register_form():
  if session.get("fullname"):
    return redirect(url_for('index'))

  return render_template('register.html')

@app.route('/register', methods = ['POST'])
def register_form_submit():
  usr = db.session.query(User.id).filter(User.email == request.form['email']).first()
  if usr:
    flash('Email exist. Please change email')
    return redirect(url_for('show_register_form'))

  user = User()
  user.fullname = request.form['fullname']
  user.phone = request.form['phone']
  user.email = request.form['email']
  user.password = request.form['password']

  db.session.add(user)
  db.session.commit()
  flash('Registration was successfully')
  return redirect(url_for('show_register_form'))

@app.route('/login', methods = ['GET'])
def show_login_form():
  if session.get("fullname"):
    return redirect(url_for('index')) 

  return render_template('login.html')

@app.route('/login', methods = ['POST'])
def login_submit():
  email = request.form['email']
  password = request.form['password']
  user = db.session.query(User.id, User.fullname).filter(User.email == email, User.password == password).first()
  if user is None:
    flash('Invalid email/password')
    return redirect(url_for('show_login_form'))  

  session["fullname"] = user.fullname
  return redirect(url_for('index'))

@app.route("/logout")
def logout():
    session["fullname"] = None
    return redirect(url_for('index'))      

if __name__ == '__main__': 
  app.run()