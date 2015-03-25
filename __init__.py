__author__ = 'aleksandrov'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import config


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app, use_native_unicode=True)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app import models, views

