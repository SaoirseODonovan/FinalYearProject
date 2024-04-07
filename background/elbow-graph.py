import numpy as np
import pandas as pd
from kmodes.kmodes import KModes
import matplotlib.pyplot as plt
np.random.seed(42)

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

data = pd.read_csv('generated_new.csv', header=None)
data.columns = questions

kmodes = KModes(n_clusters=6, init='Cao', verbose=1, random_state=42)

clusters = kmodes.fit_predict(data)
print("Cluster centroids: ")
print(kmodes.cluster_centroids_)

# For assitance with elbow method and cost function: https://codinginfinite.com/elbow-method-in-python-for-k-means-and-k-modes-clustering/, Accessed 15 January, 2024.
#https://codinginfinite.com/k-modes-clustering-for-categorical-data-in-python/
#setting a range that seems reasonable
clusters_amounts = range(1, 17)

cost = []

for cluster in clusters_amounts:
    kmodes = KModes(n_clusters=cluster, init='Cao', verbose=0, random_state=42)
    kmodes.fit(data)
    #using the cost function which should be as low as possible
    cost.append(kmodes.cost_)

plt.plot(clusters_amounts, cost, marker='*')
plt.xlabel('Cluster Number')
plt.ylabel('Cost')
plt.show()
#9 clusters is optimal k value