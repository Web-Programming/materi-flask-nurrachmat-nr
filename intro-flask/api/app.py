from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS # Import Flask-CORS

app = Flask(__name__)
# Ganti dengan kredensial MySQL Anda
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost/myflaskif31'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#akttifkan CORS
CORS(app) #mengizinkan semua domain

from routes import *

if __name__ == "__main__":
    app.run(debug=True)
