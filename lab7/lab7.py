from flask import Flask,render_template, request, redirect, url_for
import re
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db.init_app(app)

class users(db.Model):
    _id=db.Column("id",db.Integer,primary_key=True)
    firstname = db.Column("firstname",db.String(50))
    lastname = db.Column("lastname",db.String(50))
    email = db.Column("email",db.String(100),unique=True, nullable=False)
    password = db.Column("password",db.String(50), nullable=False)

@app.route('/', methods=['POST','GET'])
def signin():
    if request.method=="GET":
        return render_template('signin.html')
    email = request.form['email']
    password = request.form['psw']

    user = users.query.filter_by(email=email, password=password).first()

    if user:
        return redirect(url_for('secretpage', name=user.firstname))
    else:
        error = "Invalid username or password."
        return render_template('signin.html', error=error)


@app.route('/thankyou/<name>')
def thankyou(name):
    return render_template('thankyou.html',name=name)

@app.route('/secretpage/<name>')
def secretpage(name):
    return render_template('secretpage.html',name=name)


@app.route("/SignUp",methods=["GET","POST"])
def signup():
    if request.method=="POST":
        first_name=request.form["first_name"]
        last_name=request.form["last_name"]
        mail=request.form["email"]
        pwd=request.form["password"]
        cpwd = request.form.get('confirm_password')

        if pwd != cpwd:
            error = "Passwords do not match."
            return render_template('signup.html', error=error)
       
        if users.query.filter_by(email=mail).first():
            error_message = "Email already exists. Please use a different email address."
            return render_template('signup.html', error=error)

        
        new_user = users(firstname=first_name, lastname=last_name, email=mail, password=pwd)
        db.session.add(new_user)
        db.session.commit()
       
        
        return redirect(url_for('thankyou',name=first_name))


    else:
        return render_template('signup.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True)