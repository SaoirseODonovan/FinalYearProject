from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .cluster import questions

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def welcome():
    return render_template("welcome.html", user=current_user)

@views.route('/group', methods=['GET', 'POST'])
@login_required
def group():
    return render_template("group.html", user=current_user)

@views.route('/survey')
def survey():
    return render_template('survey.html', questions=questions)

#process the survey form
@views.route('/process_survey', methods=['POST'])
def process_survey():
    user_responses = request.form.to_dict()