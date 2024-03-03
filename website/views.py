from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from .models import Quiz
from . import db
from .cluster import get_user_category, data
from .utilities import questions, surveyQuestions
from .match import isolate_responses, current_answer
from .auth import get_current_username
from .graph import graph
import json
from flask_mail import Message

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def welcome():
    return render_template("welcome.html", user=current_user)

@views.route('/group', methods=['GET', 'POST'])
@login_required
def group():
    current_username = get_current_username()
    ans = current_answer(current_username)
    image_data = graph(data, questions)

    return render_template("group.html", user=current_user, ans=ans, image_data=image_data)

@views.route('/match', methods=['GET', 'POST'])
@login_required
def match():
    return render_template("match.html", user=current_user)

@views.route('/types', methods=['GET', 'POST'])
@login_required
def types():
    return render_template("types.html", user=current_user)

@views.route('/survey', methods=['GET', 'POST'])
@login_required
def survey():
    return render_template('survey.html', questions=questions, surveyQuestions=surveyQuestions)

def setup_views(mail):
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

            #email
            msg = Message("Your Early Days Lover Category", sender="noreply@earlydays.com", recipients=[current_user.email])
            msg.html = render_template("email.html", data={'title': 'Survey Result', 'body': user_category})
            mail.send(msg)

            return render_template('result.html', user_category=user_category)
    return views

@views.route('/check_compatibility', methods=['POST'])
@login_required
def scoring():
    if request.method == 'POST':
        selected_username = request.form.get('selected_username')
        current_username = get_current_username()
        chosen_category = request.form.get('value')

        if not_match(selected_username):
            flash('The selected user cannot be compared with.', category='error')
            return redirect(url_for('views.match'))

        score = isolate_responses(current_username, selected_username, chosen_category)
        #display using flash for now
        #will improve later
        if score is not False:
            return render_template('match.html', user=current_user, compatibility_score=score)
        else:
            flash('An error has occured. Make sure that you have first taken the survey before this step or make sure that the username you entered is valid.', category='error')

    return redirect(url_for('views.match'))

#check if user's username is in file
def not_match(username):
    with open('no_match_users.txt', 'r') as file:
        is_in_file = [line.strip() for line in file]
    return username in is_in_file