import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from recipes import app, db, mongo, mydb
from recipes.models import Cuisine, Users


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mydb.recipes.find())
    return render_template("recipes.html", recipes=recipes)


