from enum import unique
from sqlalchemy.ext.declarative import declarative_base
from ..extensions import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


Base = declarative_base()


class User(db.Model, UserMixin, Base):
    id = db.Column(db.Integer(), primary_key=True)

    username = db.Column(db.String(32), unique=True, nullable=False)
    admin = db.Column(db.Boolean, default=False)

    avatar = db.relationship('Avatar')
    avatar_id = db.Column(db.Integer, db.ForeignKey('avatar.id'))

    posts = db.relationship('Post', backref='author', lazy='dynamic')

    articles = db.relationship('Article', backref='art_author', lazy='dynamic')

    comments = db.relationship('Comment', backref='com_author', lazy='dynamic')

    premium_user = db.Column(db.Boolean, default=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    pass_hash = db.Column(db.String(120))
    created_at = db.Column(db.String, default=datetime.utcnow)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.pass_hash = generate_password_hash(password=password)

    def check_password(self, password):
        return check_password_hash(self.pass_hash, password)

class Avatar(db.Model, Base):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    url = db.Column(db.String(255), nullable=False)
    rarity = db.Column(db.String(1))
    chosen_by = db.Column(db.Integer(), default=0)

class Post(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, default=0)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Comment(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(255), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))

class Article(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    body = db.Column(db.String, nullable=False)
    created_at = db.Column(db.String, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship('Comment', backref='article', lazy='dynamic')
    theme = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, default=0)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


