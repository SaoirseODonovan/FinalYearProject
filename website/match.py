from .models import User, Quiz

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
    #where I will later add hamming distance function etc.
    #placeholder for now
    compatibility_score = 100

    return compatibility_score

