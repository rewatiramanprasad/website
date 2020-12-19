from flask import Flask,render_template,redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/raman/Desktop/webpage/datab.db'
db = SQLAlchemy(app)


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    mob = db.Column(db.Integer)

name1="raman"
@app.route("/")
def welcome():
     return "welcome to rmn wrld"
@app.route("/home")
def home():
    if request.method=="POST":
        name2=request.form('uname')
        
    return render_template("nav1.html",name=name1)
@app.route("/contactus")
def contact_us():
    return "contact me on 7250324730"

@app.route("/aboutus/<username>")
def about(username):
    return "contact me %s on 7250324730" %username

@app.route("/register",methods=["post"])
def reg(username=None):
    if request.method=="post":
        namer=request.form("name",username)
        return redirect(url_for("/aboutus/<username>",namer=username))
    
@app.route("/registration",methods=["GET","POST"])
def registration():
    if request.method=="POST":
        uname=request.form['first']
        mail=request.form['email']
        mobi=request.form['mob']
        
        
        register = user(username = uname, email = mail, mob= mobi)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["pass"]
        
        login = user.query.filter_by(username=uname, mob=passw).first()
        if login is not None:
            return redirect(url_for("home"))
    return render_template("login.html")
    


if  __name__=="__main__":
     db.create_all()
     app.run()
