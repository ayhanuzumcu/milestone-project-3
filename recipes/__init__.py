import os
from flask import Flask
from flask_pymongo import PyMongo
import pymongo
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
myclient = pymongo.MongoClient(app.config["MONGO_URI"])
mydb = myclient[app.config["MONGO_DBNAME"]]


uri = os.environ.get("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = uri  # heroku

db = SQLAlchemy(app)
mongo = PyMongo(app)

from recipes import routes  # noqa
