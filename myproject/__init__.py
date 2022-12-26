import os
from flask import Flask

from flask_migrate import Migrate

from .db import db
from myproject.puppies.views import pupy_blp
from myproject.owners.views import owners_blueprint


app=Flask(__name__)

# Often people will also separate these into a separate config.py file 
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
Migrate(app,db)
with app.app_context():
    db.create_all()
# NOTE! These imports need to come after you've defined db, otherwise you will
# get errors in your models.py files.
## Grab the blueprints from the other views.py files for each "app"


app.register_blueprint(owners_blueprint,url_prefix="/owners")
app.register_blueprint(pupy_blp,url_prefix='/puppies')
