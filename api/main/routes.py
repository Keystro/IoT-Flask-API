from flask import render_template, url_for, flash, redirect, request, Blueprint
from api.models import Vault


main = Blueprint('main',__name__)

@main.route('/data')
def data():
  devices = Vault.query.all()
  return render_template('index.html', devices=devices ,title = 'Data')

