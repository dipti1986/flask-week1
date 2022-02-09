from flask import Flask # Import Flask class
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy class
import os

app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # Create SQLALchemy object

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

class people(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(100),nullable=False)
    alive= db.Column(db.Boolean,default=True)
    height= db.Column(db.Float)


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')