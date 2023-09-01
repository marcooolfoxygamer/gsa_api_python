from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

def create_app(config_name):
    app = Flask(__name__)
    USER_DB = 'root'
    PASS_DB = 'sena'
    URL_DB = 'localhost'
    NAME_DB = 'bd_gymsenapp'
    FULL_URL_DB = f'mysql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

    app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)

    migrate = Migrate()
    migrate.init_app(app, db)
    return app
