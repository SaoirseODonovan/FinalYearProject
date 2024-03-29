from .models import User, Quiz
import json

category_questions = {
    "Family and Loyalty": [
        "Is it a dealbreaker if your partner is open to polyamorous relationships?",
        "Is it a dealbreaker if your partner has a child/children?",
        "Is it a dealbreaker if your partner does not want a child/children?"
    ],
    "Lifestyle and Habits": [
        "Is it a dealbreaker if your partner does not take care of themselves?",
        "Is it a dealbreaker if your partner is not athletic?",
        "Is it a dealbreaker if your partner is overly athletic?",
        "Is it a dealbreaker if your partner abuses substances?",
        "Is it a dealbreaker if your partner lives more than 3 hours from you?",
        "Is it a dealbreaker if your partner is lazy?",
        "Is it a dealbreaker if your partner is unambitious?",
        "Is it a dealbreaker if your partner is clingy?",
        "Is it a dealbreaker if your partner is arrogant?",
        "Is it a dealbreaker if your partner has poor personal hygiene?",
        "Is it a dealbreaker if your partner suffers from financial strain?",
        "Is it a dealbreaker if your partner suffers from mental health issues?",
        "Is it a dealbreaker if your partner suffers from health problems?"
    ],
    "Communication and Behaviour": [
        "Is it a dealbreaker if your partner is a poor communicator?",
        "Is it a dealbreaker if your partner is inconsistent?",
        "Is it a dealbreaker if your partner tends to be disrespectful to others?",
        "Is it a dealbreaker if your partner's romantic behaviors differ from yours?",
        "Is it a dealbreaker if your partner wishes to monitor your online activity?",
        "Is it a dealbreaker if your partner is secretive about their own online activity?"
    ],
    "Educational Background": [
        "Is it a dealbreaker if your partner has not completed their high school/secondary school studies?",
        "Is it a dealbreaker if your partner has not attended university or an equivalent third level institute?"
    ]
}

def current_answer(current_username):
    current_user_quiz = Quiz.query.filter_by(username=current_username).order_by(Quiz.id.desc()).first()
    current_user_answers = current_user_quiz.questions
    current_user_answers = json.loads(current_user_answers)
    current_answers_val = list(current_user_answers.values())
    return current_answers_val

def isolate_responses(current_username, selected_username, chosen_category):
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
            compatibility_result = calculate_score(current_user_answers, selected_user_answers, chosen_category)
            return compatibility_result
        else:
            return False
    else:
        return False

def calculate_score(current_user_answers, selected_user_answers, chosen_category):
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
    print("original matches: ", matches)
    if chosen_category in category_questions:
        cat_questions = category_questions[chosen_category]

        for question in cat_questions:
            current_answer = current_user_answers.get(question)
            print(current_answer)
            selected_answer = selected_user_answers.get(question)
            print(selected_answer)
            if current_answer == selected_answer:
                matches += 2
                print("new matches: ", matches)
            else:
                matches -= 1
                if matches < 0:
                    matches = 0
                print("final matches: ", matches)
            

    #round to nearest number so no decimal places 
    compatibility_score = round((matches / questions_amount) * 100)

    if compatibility_score > 100:
        compatibility_score = 100

    return compatibility_score