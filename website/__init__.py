from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

#initialize SQLAlchemy object
db = SQLAlchemy()
DB_NAME = "database.db"
path = os.getcwd()

#function to initialize flask app
def create_app():
    app = Flask(__name__ , static_folder="static")
    app.config['SECRET_KEY'] = 'a402cd29cade63e402342cb2'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['MAX_CONTENT_PATH'] = 26214400
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .models import User

    #views and auth are blueprint objects
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    with app.app_context():
        #uncomment when making database modifications
        #db.drop_all()
        db.create_all()

    Login_mngr = LoginManager()
    Login_mngr.login_view = 'auth.login'
    Login_mngr.init_app(app)

    @Login_mngr.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app