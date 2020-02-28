from flask import render_template, url_for, flash, redirect, request, Blueprint
from api.models import IOTS


main = Blueprint('main',__name__)

@main.route('/data')
def data():
  devices = IOTS.query.all()
  return render_template('index.html', devices=devices ,title = 'Data')

