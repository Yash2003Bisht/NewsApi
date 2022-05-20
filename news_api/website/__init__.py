from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from .json_data import getData
from concurrent.futures import ThreadPoolExecutor

db = SQLAlchemy()


def webApp():
    """creating app"""
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    from .models import NewsData
    createDataBase(app, NewsData)
    return app


def createDataBase(app, NewsData):
    """creating database if not exists"""
    if not os.path.exists("website/database.db"):
        data = getData()
        db.create_all(app=app)
        add_data(NewsData, data)


def add_data(NewsData, data):
    """Adding news data to database"""
    app = webApp()
    with app.app_context():
        for i in range(len(data)):
            add_json_data = NewsData(
                title_en=data[i]["title_en"],
                desc_en=data[i]["desc_en"],
                title_fr=data[i]["title_fr"],
                desc_fr=data[i]["desc_fr"],
                timestamp=data[i]["timestamp"],
                image_url=data[i]["image_url"]
            )
            db.session.add(add_json_data)
            db.session.commit()
