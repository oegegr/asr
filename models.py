__author__ = 'aleksandrov'

from app import db


class Printers(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Directory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String, unique=True)
    color = db.Column(db.Boolean)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturers.id'))

class Manufacturers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String, unique=True)
    printer_type = db.relationship('Directory', backref='manufacturer', lazy='dynamic')

    @staticmethod
    def get_manufacturer():
        manufacturers = db.session.query(Manufacturers.manufacturer)
        result = []
        for el in manufacturers:
            result.append((el[0], el[0]))
        return result



