from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# Config Values
USERNAME = 'admin'
PASSWORD = 'password123'

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'Sup3r$3cretkey'

app = Flask(__name__)
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = "./app/static/images"
filefolder = app.config['UPLOAD_FOLDER']


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://tpccwcbrsiczjk:b19bd7335339862af8cd7e545034cccdd94a7e7074e2acf35ddf58392faa0317@ec2-75-101-133-29.compute-1.amazonaws.com:5432/de1qbii0vij0tq"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
db = SQLAlchemy(app)


# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = "info"  # customize the flash message category

from app import views