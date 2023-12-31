from flask import Flask,render_template, request
import re
from flaskext.mysql import MySQL
app=Flask(__name__)
mysql = MySQL(autocommit=True)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Smallworld@9286'
app.config['MYSQL_DATABASE_DB'] = 'employee'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = '3306'
mysql.init_app(app)

count=0
@app.route('/')
def base():
    return render_template('base.html')

@app.route('/SignUp')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    Username=request.args.get('Username')
    Password=request.args.get('Password')
    message="</br><ul>"
    global count
    flag=0
    premsg="<h3>Oh no! Looks like you had issues with your password.<h3></br><p>Here are the requirenments:</p></br> "
    if (len(Password)<8):
        flag = -1
        message=message+"<li>looks like your Password is less that 8 Characters</li> "
    if not (re.search("[a-z]", Password)):
        flag = -1
        message=message+"<li>looks like your Password does not contain lower case letters</li> "
    if not (re.search("[A-Z]", Password)):
        flag = -1
        message=message+"<li>looks like your Password does not contain Upper case letters</li> "
    if not (Password[-1].isdigit()):
        flag = -1
        message=message+"<li>looks like your Password does not end with a digit</li> "
    if(flag==0):
        count=0
        message="<h3>Your Password Passed the Requirements<h3>"
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("INSERT INTO uname(username, password) VALUES (%s, %s)", (Username, Password))


        cursor.close()
        
 
    if flag == -1:
        count+=1
        # print("count: ",count)
        message=premsg+message+"</ul>"

    if(count<3):
        return render_template('report.html',Username=Username,Password=Password,message=message)
    else:
        return render_template('warning.html')


if __name__ == '__main__':
    app.run()