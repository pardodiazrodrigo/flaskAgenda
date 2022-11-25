from flask import Blueprint, render_template

contacts = Blueprint('contacts', __name__)


@contacts.route('/')
def home():
    return render_template('home.html')


@contacts.route('/new')
def add_contact():
    return "Saving contact"


@contacts.route('/update')
def update():
    return "update contact"


@contacts.route('/delete')
def delete():
    return "delete contact"


@contacts.route('/about')
def about():
    return render_template('about.html')
