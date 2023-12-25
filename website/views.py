from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .models import Quiz, User
from . import db
from .cluster import questions, get_user_category

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
    if request.method == 'POST':
        user_responses = request.form.to_dict()
        
        #save to database
        quiz = Quiz(username=current_user.username, **user_responses)
        db.session.add(quiz)
        db.session.commit()

        return render_template('result.html')

    return render_template('survey.html', questions=questions)

#process the survey form
@views.route('/process_survey', methods=['POST'])
def process_survey():
    if request.method == 'POST':

            user_responses = request.form.to_dict()
            #get category
            user_category = get_user_category(user_responses)
   
            return render_template('result.html', cluster=user_category)