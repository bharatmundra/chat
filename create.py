from flask import Flask
from models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgres://pljzpkgljwqeiu:2e810b076f432df14cd089fb7207e7cdfa6f96c528c892b9ad96d0df24c4f1ec@ec2-44-193-178-122.compute-1.amazonaws.com:5432/d8im41dkh59lke'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()