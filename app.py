from flask import Flask,render_template

from wtform_field import *
from models import *
app=Flask(__name__)

app.secret_key='replcee_later'

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://pljzpkgljwqeiu:2e810b076f432df14cd089fb7207e7cdfa6f96c528c892b9ad96d0df24c4f1ec@ec2-44-193-178-122.compute-1.amazonaws.com:5432/d8im41dkh59lke'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

@app.route("/",methods=['GET', 'POST'])
def index():
    
    reg_form=RegistrationForm()
    if reg_form.validate_on_submit():
        username=reg_form.username.data
        password=reg_form.password.data
        user_object=User.query.filter_by(username=username).first()
        if user_object:
           return "username already exist. select a differnt username."

        user = User(username=username,password=password)  
        db.session.add(user)
        db.session.commit()
        return "inserted into DB!"


    return render_template("index.html",form=reg_form)



if __name__=="__main__":
    app.run(debug=True)