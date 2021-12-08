# pylint: disable=no-member

from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    """
    Whenever we call this function by clicking the navbar link for Categories,
    it will query the database and retrieve all records from this table,
    then sort them by the category name.
    this variable is passed into our rendered template,
    so that we can use this data to display everything to our users.
    By using the all() method, this is actually what's known as a Cursor Object
    The first declaration of 'categories' is the variable name
    that we can now use within the HTML template.
    The second 'categories', which is now a list(),
    is the variable defined within our function
    """
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    When a user clicks the "Add Category" button,
    this will use the "GET" method and render the 'add_category' template.
    Once they submit the form, this will call the same function,
    but will check if the request
    being made is a “POST“ method, which posts data to the database.
    """
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """
    we've given an argument of 'category_id' when clicking the 'Edit' button,
    this also needs to appear in our app.route.
    These types of variables being passed back into our Python functions
    must be wrapped inside of angle-brackets within the URL.
    We also need to pass the variable directly into the function as well,
    so we have the value available to use within this function.
    """
    category = Category.query.get_or_404(category_id)
    """
    There's a SQLAlchemy method called '.get_or_404()',
    which takes the argument of 'category_id'.
    What this does is query the database
    and attempts to find the specified record using the data
    provided, and if no match is found,
    it will trigger a 404 error page.
    """
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)
