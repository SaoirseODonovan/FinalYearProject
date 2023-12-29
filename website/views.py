from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .models import Quiz, User
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

@views.route('/survey', methods=['GET', 'POST'])
@login_required
def survey():
    return render_template('survey.html', questions=questions)
   
@views.route('/process_survey', methods=['POST'])
def process_survey():

    if request.method == 'POST':
        user_responses = request.form.to_dict()
        user_category = get_user_category(user_responses)

        user_responses = {}
        
        for question in questions:
            user_responses[question] = request.form.get(question)

        #convert to dict
        responses_json = json.dumps(user_responses)

        quiz = Quiz(username=current_user.username, questions=responses_json)
        db.session.add(quiz)
        db.session.commit()

        # Get category

        return render_template('result.html', user_category=user_category)

            