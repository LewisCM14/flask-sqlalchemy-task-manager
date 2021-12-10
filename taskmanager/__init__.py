"""
This file ensures our task manager application
is initalized as a package
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa

# create instance of imported flask class
app = Flask(__name__)

# app config variables, based on environ variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

# create instance of sqlalchemy class
db = SQLAlchemy(app)

from taskmanager import routes  # noqa
