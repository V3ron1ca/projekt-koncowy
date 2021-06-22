from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///database.db"
app.config.from_object(Config)
db = SQLAlchemy(app)

from .models import Entry
import blog.routes

migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Entry": models.Entry
    }
