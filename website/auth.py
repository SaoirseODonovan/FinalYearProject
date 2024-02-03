from flask import Blueprint, render_template, request, flash, redirect, url_for
#blueprint allows for grouping related templates, views etc.
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db #database imported from __init__.py
from flask_login import login_user, login_required, logout_user, current_user 

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():

    login_invalid_fields = []

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Login was successful!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.welcome'))
            else:
                flash('Password was incorrect!', category='error')
                login_invalid_fields.append('password')
        else:
            flash('Email does not exist!', category='error')
            login_invalid_fields.append('email')

    return render_template("login.html", user=current_user, invalid_fields=login_invalid_fields)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():

    sign_invalid_fields = []

    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        pronouns = request.form.get('pronouns')
        opt_out = 'optOut' in request.form

        email_exist = User.query.filter_by(email=email).first()
        username_exist = User.query.filter_by(username=username).first()
        if email_exist:
            flash('Email already exists.', category='error')
            sign_invalid_fields.append('email')
        elif username_exist:
            flash('Username already exists.', category='error')
            sign_invalid_fields.append('username')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
            sign_invalid_fields.append('email')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
            sign_invalid_fields.append('firstName')
        elif len(username) < 4:
            flash('Username must be at least 4 characters.', category='error')
            sign_invalid_fields.append('username')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, username=username, pronouns=pronouns, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            #persist changes to db
            db.session.commit()

            if opt_out:
                with open('no_match_users.txt', 'a') as file:
                    file.write(username + '\n')

            login_user(new_user, remember=True)
            flash('Account created!', category='success')

            return redirect(url_for('views.welcome'))


    return render_template("signup.html", user=current_user, invalid_fields=sign_invalid_fields)

def get_current_username():
    if current_user.is_authenticated:
        return current_user.username
    else:
        return None