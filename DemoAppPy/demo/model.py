from flask_sqlalchemy import SQLAlchemy 
from flask import Flask, jsonify, request
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()
 
class User(UserMixin, db.Model):
    __tablename__ = 'registration'    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(150), unique = True, index = True)
    password_hash = db.Column(db.String(150))
    joined_at = db.Column(db.DateTime(), default = datetime.utcnow, index = True)

    # def set_password(self, password):
    #         self.password_hash = generate_password_hash(password)

    # def check_password(self,password):
    #     return check_password_hash(self.password_hash,password)

    def __init__(self,id,username,email,password_hash,joined_at):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.joined_at = joined_at
        
    def __repr__(self):
        return self    


