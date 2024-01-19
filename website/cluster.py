import numpy as np
import pandas as pd
from kmodes.kmodes import KModes

# For assistance with KModes usage: https://pypi.org/project/kmodes/ Accessed January 11, 2024. 

#adding a random seed ensures that the attributes associated with each cluster will not change each time that the code is run 
np.random.seed(42)

#sample questions
questions = [
    'Is it a dealbreaker if your partner is open to polyamorous relationships? ',
    'Is it a dealbreaker if your partner has a child/children? ',
    'Is it a dealbreaker if your partner does not want a child/children? ',
    'Is it a dealbreaker if your partner does not take care of themselves? ',
    'Is it a dealbreaker if your partner is not athletic? ',
    'Is it a dealbreaker if your partner is overly athletic? ',
    'Is it a dealbreaker if your partner abuses substances? ',
    'Is it a dealbreaker if your partner lives more than 3 hours from you? ',
    'Is it a dealbreaker if your partner is lazy?',
    'Is it a dealbreaker if your partner is unambitious?',
    'Is it a dealbreaker if your partner is clingy?',
    'Is it a dealbreaker if your partner is arrogant?',
    'Is it a dealbreaker if your partner has poor personal hygiene?',
    'Is it a dealbreaker if your partner is a poor communicator?',
    'Is it a dealbreaker if your partner is inconsistent?',
    'Is it a dealbreaker if your partner tends to be disrespectful to others?',
    'Is it a dealbreaker if your partners romantic behaviours differ from yours? e.g. differing love languages, methods of expressing romatic feelings. ',
    'Is it a dealbreaker if your partner wishes to monitor your online activity? e.g. looking though text messages, content watched, social media posts and communications.  ',
    'Is it a dealbreaker if your partner is secretive about their own online activity? ',
    'Is it a dealbreaker if your partner suffers from financial strain?',
    'Is it a dealbreaker if your partner has not completed their high school/secondary school studies?',
    'Is it a dealbreaker if your partner has not attended university or an equivalent third level institute?',
    'Is it a dealbreaker if your partner suffers from mental health issues?',
    'Is it a dealbreaker if your partner suffers from health problems?',
]

#get data from generated, expanded dataset
data = pd.read_csv('generated_data.csv', header=None)
data.columns = questions

#no need for encoding anymore as kmodes handles categoric data unlike kmeans
#initialise k-modes clustering
#four clusters for now
#Cao is a common initialisation method for starting
kmodes = KModes(n_clusters=9, init='Cao', verbose=1, random_state=42)

clusters = kmodes.fit_predict(data)
print("Cluster centroids: ")
print(kmodes.cluster_centroids_)
cluster_types = { 0: "Category 1", 1: "Category 2", 2: "Category 3", 3: "Category 4", 4: "Category 5", 5: "Category 6", 6: "Category 7", 7: "Category 8", 8: "Category 9" }

def preprocess_user_responses(user_responses):
    #create a dataframe from user responses
    user_df = pd.DataFrame([user_responses.values()], columns=questions)
    print(user_df)

# For assistance with .to_csv: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html Accessed January 19, 2024.
    
    #ordering
    user_df_csv = user_df.reindex(columns=questions)
    #mode='a' appends user survey responses to the csv
    #leave out column names and index 
    user_df_csv.to_csv('generated_data.csv', mode='a', header=False, index=False)

    return user_df

#applies model to assign a cluster to the user, where a cluster is associated with a named category
def get_user_category(user_responses):
    user_df = preprocess_user_responses(user_responses)
    user_cluster = kmodes.predict(user_df)
    user_category = f"{cluster_types[user_cluster[0]]}"
    print("User category in func is: ")
    print(user_category)
    return user_category

#testing
user_responses = {
    'Is it a dealbreaker if your partner is open to polyamorous relationships? ': 'Not Sure',
    'Is it a dealbreaker if your partner has a child/children? ': 'Yes',
    'Is it a dealbreaker if your partner does not want a child/children? ': 'No',
    'Is it a dealbreaker if your partner does not take care of themselves? ': 'No',
    'Is it a dealbreaker if your partner is not athletic? ': 'Yes',
    'Is it a dealbreaker if your partner is overly athletic? ': 'Not Sure',
    'Is it a dealbreaker if your partner abuses substances? ': 'No',
    'Is it a dealbreaker if your partner lives more than 3 hours from you? ': 'Yes',
    'Is it a dealbreaker if your partner is lazy?': 'No',
    'Is it a dealbreaker if your partner is unambitious?': 'Yes',
    'Is it a dealbreaker if your partner is clingy?': 'No',
    'Is it a dealbreaker if your partner is arrogant?': 'No',
    'Is it a dealbreaker if your partner has poor personal hygiene?': 'Not Sure',
    'Is it a dealbreaker if your partner is a poor communicator?': 'Yes',
    'Is it a dealbreaker if your partner is inconsistent?': 'No',
    'Is it a dealbreaker if your partner tends to be disrespectful to others?': 'Not Sure',
    'Is it a dealbreaker if your partners romantic behaviours differ from yours? e.g. differing love languages, methods of expressing romatic feelings. ': 'No',
    'Is it a dealbreaker if your partner wishes to monitor your online activity? e.g. looking though text messages, content watched, social media posts and communications.  ': 'Yes',
    'Is it a dealbreaker if your partner is secretive about their own online activity? ': 'Yes',
    'Is it a dealbreaker if your partner suffers from financial strain?': 'Yes',
    'Is it a dealbreaker if your partner has not completed their high school/secondary school studies?': 'No',
    'Is it a dealbreaker if your partner has not attended university or an equivalent third level institute?': 'Yes',
    'Is it a dealbreaker if your partner suffers from mental health issues?': 'Indifferent',
    'Is it a dealbreaker if your partner suffers from health problems?': 'Yes',
}

category = get_user_category(user_responses)
print(category)