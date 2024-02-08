from flask_sqlalchemy import SQLAlchemy
from  app import db




#creating a table for store contact information
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=True , nullable=False)
    password=db.Column(db.String(80),unique=False,nullable=False)
    email=db.Column(db.String(80),unique=False , nullable=False)
    phone_num=db.Column(db.String(12),unique=True , nullable=False)
    msg=db.Column(db.Text,unique=False , nullable=False)
    date=db.Column(db.String(12),unique=False , nullable=False)

