from flask import Flask
from routes.contacts import contacts
from settings import DATABASE_CONNECTION_URI


app = Flask(__name__)
app.secret_key = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.register_blueprint(contacts)
