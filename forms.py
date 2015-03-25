__author__ = 'aleksandrov'
from flask_wtf import Form
from wtforms import StringField, BooleanField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from .models import Manufacturers



class AddManufacturerForm(Form):
    manufacturer = StringField('manufacturer')


class AddPrinter(Form):
    manufacturer = QuerySelectField('manufacturer', choices=Manufacturers.get_manufacturer())
    model = StringField('model')
    color = BooleanField('color')