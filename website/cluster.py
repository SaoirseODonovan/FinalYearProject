import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

#sample questions
questions = [
    'Your partner does not want a kid(s)?',
    'Your partner has a kid(s)?',
    'Your partner has been previously divorced?',
    'Your partners parents are divorced?',
    'Your partner has bad hygiene?',
    'Your partner is not athletic?',
    'Your partner did not complete high school?',
    'Your partner did not attend University?',
    'Your partner is unemployed?',
    'Your partner still lives at home?',
    'Your partner smokes?',
    'Your partner drinks alcohol?',
    'Your partner vapes?',
    'Your partner has cheated in the past?',
    'Your partner is still close with an ex partner of theirs?',
    'Your partner is clingy?',
    'Your partner is dishonest?',
    'Your partner is vegan?',
    'Your partner keeps you a secret?',
    'Your partner is excessively jealous?',
]

#preprocess and encode user responses
def preprocess_user_responses(user_responses):
    #create a dataframe from user responses
    user_df = pd.DataFrame([user_responses.values()], columns=questions)

#For assistance with LabelEncoder usage: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html Accessed December 5, 2023.
    #encode categorical responses
    label_encoder = LabelEncoder()
    for column in user_df.columns:
        user_df[column] = label_encoder.fit_transform(user_df[column])

    return user_df

def convert_cluster_to_category(cluster):
    categories = ["The stringent lover", "The unbiased lover", "The flexible lover", "The explorative lover"]
    return categories[cluster]

#For assistance with KMeans clustering + resources gained from Data Mining module: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html Accessed December 2, 2023.
#initialise k-means clustering
kmeans = KMeans(n_clusters=4, random_state=42)

if questions != "":
#sample data
    data = {
        'Your partner does not want a kid(s)?': [0, 0, 0, 1],
        'Your partner has a kid(s)?': [0, 0, 1, 0],
        'Your partner has been previously divorced?': [0, 0, 1, 0],
        'Your partners parents are divorced?': [0, 0, 0, 1],
        'Your partner has bad hygiene?': [1, 0, 0, 0],
        'Your partner is not athletic?': [0, 1, 0, 0],
        'Your partner did not complete high school?': [0, 1, 0, 0],
        'Your partner did not attend University?': [1, 0, 0, 0],
        'Your partner is unemployed?': [0, 0, 1, 0],
        'Your partner still lives at home?': [0, 0, 0, 1],
        'Your partner smokes?': [0, 0, 1, 0],
        'Your partner drinks alcohol?': [0, 0, 0, 1],
        'Your partner vapes?': [1, 0, 0, 0],
        'Your partner has cheated in the past?': [0, 1, 0, 0],
        'Your partner is still close with an ex partner of theirs?': [0, 0, 0, 1],
        'Your partner is clingy?': [1, 0, 0, 0],
        'Your partner is dishonest?': [0, 0, 1, 0],
        'Your partner is vegan?': [0, 1, 0, 0],
        'Your partner keeps you a secret?': [0, 0, 0, 1],
        'Your partner is excessively jealous?': [1, 0, 0, 0],
    }

    kmeans.fit(pd.DataFrame(data))

#applies model to assign a cluster to the user, where a cluster is associated with a named category
def get_user_category(user_responses):
    user_df = preprocess_user_responses(user_responses)
    user_cluster = kmeans.predict(user_df)
    #right now default is cluster 0 
    user_category = convert_cluster_to_category(user_cluster[0])
    return user_category