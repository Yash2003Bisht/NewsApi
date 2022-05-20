from . import db

class NewsData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title_en = db.Column(db.String(500), nullable=False)
    desc_en = db.Column(db.String(500), nullable=False)
    title_fr = db.Column(db.String(500), nullable=False)
    desc_fr = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.String(500), nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
