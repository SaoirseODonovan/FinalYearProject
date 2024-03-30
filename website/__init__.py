#For assistance with flask sign up, login and database (SQLAlchemy) usage: https://youtu.be/uZnp21fu8TQ?si=i165JQRHuDr-G8hO Accessed December 13, 2023.
#For assistance with setting up mail configurations: https://www.youtube.com/watch?v=nOkpTwPvDTg Accessed March 3, 2024.
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail, Message
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
    app.config['MAIL_SERVER'] = "smtp.googlemail.com"
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'noreply.earlydays@gmail.com'
    app.config['MAIL_PASSWORD'] = 'duik xyxf kxho atgj'
    app.config['MAX_CONTENT_PATH'] = 26214400
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    db.init_app(app)

    from .views import views, setup_views
    from .auth import auth
    from .models import User

    mail = Mail(app)
    app.register_blueprint(setup_views(mail), url_prefix='/')

    #views and auth are blueprint objects
    # app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    with app.app_context():
        #uncomment when making database modifications
        db.drop_all()
        #db.create_all()

    Login_mngr = LoginManager()
    Login_mngr.login_view = 'auth.login'
    Login_mngr.init_app(app)

    @Login_mngr.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app