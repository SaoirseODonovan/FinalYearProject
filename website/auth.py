import os
from flask import Blueprint, current_app, render_template, request, flash, redirect, send_from_directory, url_for
#blueprint allows for grouping related templates, views etc.
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db #database imported from __init__.py
from flask_login import login_user, login_required, logout_user, current_user
import pyotp
import qrcode

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():

    login_invalid_fields = []

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        code = request.form.get('2fa_code')
        skip_2fa = request.form.get('2fa_skip')

        user = User.query.filter_by(email=email).first()

        if user:
            if not os.path.isfile('2fa.txt'):
                open('2fa.txt', 'w').close()

            with open('2fa.txt', 'r') as file:
                users_2fa = file.readlines()
            users_2fa = [username.strip() for username in users_2fa]

            if user.username in users_2fa:
                if code:
                    if ' ' in code:
                        flash('The 2FA code entered should not contain any spaces.', category='error')
                        return render_template("login.html", user=current_user, invalid_fields=login_invalid_fields)

                    totp = pyotp.TOTP(user.secret_key)
                    if not totp.verify(code):
                        flash('Invalid 2FA code entered!', category='error')
                        return render_template("login.html", user=current_user, invalid_fields=login_invalid_fields)
                else:
                    flash('You must enter a 2FA code.', category='error')
                    return render_template("login.html", user=current_user, invalid_fields=login_invalid_fields)

            if check_password_hash(user.password, password):
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

@auth.route('/privacy_policy.txt')
def privacy_policy():
    dir = os.path.dirname(os.path.realpath(__file__))
    return send_from_directory(dir, 'privacy_policy.txt')

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
            if password1 == password2 and not User.query.filter_by(email=email).first():
                key = pyotp.random_base32()
                uri = pyotp.totp.TOTP(key).provisioning_uri(name=email, issuer_name='Early Days')

                tmp_dir = os.path.join(current_app.root_path, 'static', 'tmp')
                os.makedirs(tmp_dir, exist_ok=True)

                #save temporarily for displaying qr code
                path_relative = os.path.join('tmp', f'{username}_qr_code.png').replace("\\", "/")
                qr_path = os.path.join(current_app.root_path, 'static', path_relative)
                qr = qrcode.make(uri)
                qr.save(qr_path)

                new_user = User(email=email, first_name=first_name, username=username, pronouns=pronouns, password=generate_password_hash(
                password1, method='pbkdf2:sha256'), secret_key=key)
                db.session.add(new_user)
            #persist changes to db
                db.session.commit()

                if opt_out:
                    with open('no_match_users.txt', 'a') as file:
                        file.write(username + '\n')

                login_user(new_user, remember=True)
                flash('User created successfully! Make sure to scan the QR code with your chosen 2FA app, or skip this step for now.', category='success')
                return render_template("2fa.html", qr_path=path_relative, user_id=new_user.id)
            else:
                flash('Error in signup details.', category='error')


    return render_template("signup.html", user=current_user, invalid_fields=sign_invalid_fields)

def get_current_username():
    if current_user.is_authenticated:
        return current_user.username
    else:
        return None
    
@auth.route('/2fa', methods=['POST'])
def twofa():
    user_id = request.form.get('user_id')
    if request.form.get('scanned'):
        user = User.query.get(user_id)
        if user:
            if not os.path.isfile('2fa.txt'):
                open('2fa.txt', 'w').close()

            with open('2fa.txt', 'a') as file:
                file.write(user.username + '\n')
            
            login_user(user, remember=True)

            img_path = os.path.join(current_app.root_path, 'static', 'tmp')
            for file in os.listdir(img_path):
                path = os.path.join(img_path, file)
                try:
                    if os.path.isfile(path):
                        os.remove(path)
                except Exception as e:
                    flash(f"Error with deletion: {e}", category='error')

            return redirect(url_for('views.welcome'))
    
    flash("Make sure that you have scanned the QR code, you will not have another opportunity to do so.", category='error')
    return redirect(url_for('auth.signup'))
