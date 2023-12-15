from . import db
from flask_login import UserMixin

#usermixin defines id attribute 
#db.model is used for SQLAlchemy models
#nullable=False means it cannot be empty 
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    pronouns = db.Column(db.String(100))