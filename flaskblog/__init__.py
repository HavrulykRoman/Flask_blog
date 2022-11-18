from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8eea62aeffa25a3ae5ba99fa0eea6c81'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db: SQLAlchemy = SQLAlchemy(app)

from flaskblog import routes