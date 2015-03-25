__author__ = 'aleksandrov'
from app import app
from flask import render_template, url_for, redirect
from app import forms, db, models
from .forms import AddManufacturerForm, AddPrinter
from .models import Manufacturers, Directory


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/directory')
def directory():
    return ''


@app.route('/addmanufacturer', methods=['GET', 'POST'])
def addmanufacturer():
    form = AddManufacturerForm()
    if form.validate_on_submit():
        manufacturer = Manufacturers(manufacturer=form.manufacturer.data)
        db.session.add(manufacturer)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addmanufacturer.html', form=form)


@app.route('/addprinter', methods=['GET', 'POST'])
def addprinter():
    form = AddPrinter()
    if form.validate_on_submit():
        directory = Directory(model=form.model.data,
                              color=form.color.data,
                              manufacurer_id=Manufacturers.query.filter_by(form.manufacturer.data).first())
        db.session.add(directory)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addprinter.html', form=form)