from src.ext import db
class Tour(db.Model):
    __tablename__ = "tours"
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String)
    title = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Float)
    currency = db.Column(db.String)
    image = db.Column(db.String)
    duration = db.Column(db.String)