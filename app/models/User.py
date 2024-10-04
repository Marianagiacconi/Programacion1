from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Enum

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(Enum('user', 'admin'), default='user')  # Rol por defecto es 'user'
    poems = db.relationship('Poem', backref='author', lazy=True)
    reviews = db.relationship('Review', backref='reviewer', lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
