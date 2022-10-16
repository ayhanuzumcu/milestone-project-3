import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from recipes import app, db, mongo, mydb
from recipes.models import Cuisine, Users


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mydb.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already registered in db
        existing_user = Users.query.filter(
            Users.user_name == request.form.get("username").lower()).all()
        
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        
        user =Users(
            user_name=request.form.get("username").lower(),
            password=generate_password_hash(request.form.get("password"))
        )

        db.session.add(user)
        db.session.commit()

        new_user = Users.query.get_or_404(user.id)

        session["user"] = request.form.get("username").lower()
        flash("Registration successful")
        return redirect(url_for("profile", user_name=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = Users.query.filter(
            Users.user_name == request.form.get("username").lower()).all()

        if existing_user:
            print(request.form.get("username"))
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user[0].password, request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(request.form.get("username")))
                        return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
        
    if "user" in session:
        return render_template("profile.html", username=session["user"])

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "cuisine_name": request.form.get("cuisine_name"),
            "recipe_name": request.form.get("recipe_name"),
            "prep_time": request.form.get("prep_time"),
            "cooking_time": request.form.get("cooking_time"),
            "serves": request.form.get("serves"),
            "ingredients": request.form.get("ingredients"),
            "instructions": request.form.get("instructions"),
            "img_url": request.form.get("img_url"),
            "created_by": session["user"]
        }
        mycol = mydb["recipes"]
        mycol.insert_one(recipe)  
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))
    cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_name).all())
    return render_template("add_recipe.html", cuisines=cuisines)


# @app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
# def edit_recipe():
#     if request.method == "POST":
#         submit = {
#             "cuisine_name": request.form.get("cuisine_name"),
#             "recipe_name": request.form.get("recipe_name"),
#             "prep_time": request.form.get("prep_time"),
#             "cooking_time": request.form.get("cooking_time"),
#             "serves": request.form.get("serves"),
#             "ingredients": request.form.get("ingredients"),
#             "instructions": request.form.get("instructions"),
#             "img_url": request.form.get("img_url"),
#             "created_by": session["user"]
#         }
#         mycol = mydb["recipes"]
#         mycol.update_one({"_id": ObjectId(recipe_id)}, { "$set": submit })  
#         flash("Recipe Successfully Updated")

#     recipe = mydb["recipes"].find_one({"_id": ObjectId(recipe_id)})

#     cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_name).all())
#     return render_template("edit_recipe.html", recipe=recipe, cuisines=cuisines)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    
    recipe = mydb["recipes"].find_one({"_id": ObjectId(recipe_id)})

    # if "user" not in session or session["user"] != task["created_by"]:
    #     flash("You can only edit your own tasks!")
    #     return redirect(url_for("get_tasks"))

    if request.method == "POST":
        
        submit = {
            "cuisine_name": request.form.get("cuisine_name"),
            "recipe_name": request.form.get("recipe_name"),
            "prep_time": request.form.get("prep_time"),
            "cooking_time": request.form.get("cooking_time"),
            "serves": request.form.get("serves"),
            "ingredients": request.form.get("ingredients"),
            "instructions": request.form.get("instructions"),
            "img_url": request.form.get("img_url"),
            "created_by": session["user"]
        }
        # mycol = mydb["recipes"]
        mydb["recipes"].update_one({"_id": ObjectId(recipe_id)}, { "$set": submit })
        flash("Recipe Successfully Updated")
        return redirect(url_for("get_recipes"))
        

        # mongo.db.tasks.update({"_id": ObjectId(task_id)}, submit)
        # flash("Task Successfully Updated")

    # categories = list(Category.query.order_by(Category.category_name).all())
    # return render_template("edit_task.html", task=task, categories=categories)

    cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_name).all())
    return render_template("edit_recipe.html", recipe=recipe, cuisines=cuisines)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):

    recipe = mydb["recipes"].find_one({"_id": ObjectId(recipe_id)})

    if "user" not in session or session["user"] != recipe["created_by"]:
        flash("You can only delete your own tasks!")
        return redirect(url_for("get_tasks"))

    mydb["recipes"].delete_one({"_id": ObjectId(recipe_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("get_recipes"))