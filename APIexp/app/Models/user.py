from app import db

class UserInfo(db.Model):
    __tablename__ = 'userinfo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.Integer, nullable=True)