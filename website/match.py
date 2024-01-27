from .models import User, Quiz
from scipy.spatial import distance
import json

def current_answer(current_username):
    current_user_quiz = Quiz.query.filter_by(username=current_username).order_by(Quiz.id.desc()).first()
    current_user_answers = current_user_quiz.questions
    current_user_answers = json.loads(current_user_answers)
    current_answers_val = list(current_user_answers.values())
    return current_answers_val

def isolate_responses(current_username, selected_username):
    #just like the process used in auth.py with email
    selected_user = User.query.filter_by(username=selected_username).first()
    
    if selected_user:
        #.desc for id in descending order
        #this way I can access the latest quiz answers 
        current_user_quiz = Quiz.query.filter_by(username=current_username).order_by(Quiz.id.desc()).first()
        selected_user_quiz = Quiz.query.filter_by(username=selected_username).order_by(Quiz.id.desc()).first()
        
        if current_user_quiz and selected_user_quiz:
            current_user_answers = current_user_quiz.questions
            selected_user_answers = selected_user_quiz.questions
            compatibility_result = calculate_score(current_user_answers, selected_user_answers)
            return compatibility_result
        else:
            return False
    else:
        return False

def calculate_score(current_user_answers, selected_user_answers):
    #had to alter my approach since the change to handling categoric data meant that the Hamming distance function would not be suitable

    # For assistance with converting JSON formatted strings to lists: https://www.programiz.com/python-programming/json Accessed January 21, 2024.
    #need to access all exact answers
    current_user_answers = json.loads(current_user_answers)
    selected_user_answers = json.loads(selected_user_answers)
    current_answers_val = list(current_user_answers.values())
    selected_answers_val = list(selected_user_answers.values())

    questions_amount = 24
    #get amount of matches
    matches = sum(
        current_answer == selected_answer
        #was getting error: ValueError: too many values to unpack (expected 2)
        #so need to add zip, plus it is needed so that corresponding answers to questions will be compared
        #compares two answers one by one
        # For assistance for zip() function: https://www.w3schools.com/python/ref_func_zip.asp Accessed January 22, 2024.
        for current_answer, selected_answer in zip(current_answers_val, selected_answers_val)
        )
    #round to nearest number so no decimal places 
    compatibility_score = round((matches / questions_amount) * 100)
    return compatibility_score