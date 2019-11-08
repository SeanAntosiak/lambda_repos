"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask
import openaq
from flask_sqlalchemy import SQLAlchemy


APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB = SQLAlchemy(APP)


@APP.route('/')
def root():
    return str(Record.query.filter(Record.value >= 10).all())


def initVals():

    api = openaq.OpenAQ()

    status, body = api.measurements(city='Los Angeles', parameter='pm25')

    vals = []
    for i in range(len(body['results'])):
        tim = body['results'][i]['date']['utc']
        val = body['results'][i]['value']
        tup = (tim, val)
        vals.append(tup)
    return(vals)


class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return f'< Time: {self.datetime}  ---   Date: {self.value} >'


@APP.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()

    vals = initVals()

    for rec in vals:
        aRec = Record(datetime=rec[0], value=rec[1])
        DB.session.add(aRec)

    DB.session.commit()

    return 'Data refreshed!'
