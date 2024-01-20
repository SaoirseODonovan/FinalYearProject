from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from .models import Quiz
from . import db
from .cluster import questions, get_user_category
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def welcome():
    return render_template("welcome.html", user=current_user)

@views.route('/group', methods=['GET', 'POST'])
@login_required
def group():
    return render_template("group.html", user=current_user)

@views.route('/match', methods=['GET', 'POST'])
@login_required
def match():
    return render_template("match.html", user=current_user)

@views.route('/survey', methods=['GET', 'POST'])
@login_required
def survey():
    return render_template('survey.html', questions=questions)
   
@views.route('/process_survey', methods=['POST'])
def process_survey():

    if request.method == 'POST':
        user_responses = request.form.to_dict()

        #check questions not answered 
        for question in questions:
            if not user_responses.get(question):
                flash(f'Please do not leave any questions blank.', category='error')
                #redirect back to survey
                return redirect(url_for('views.survey'))

        user_category = get_user_category(user_responses)

        #convert to dict
        responses_json = json.dumps(user_responses)

        quiz = Quiz(username=current_user.username, questions=responses_json)
        db.session.add(quiz)
        db.session.commit()

        return render_template('result.html', user_category=user_category)