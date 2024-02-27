#the purpose of this file is to take the small dataset from the gathered surey responses and generate a larger dataset based on the answers to make all clustering computations more accurate
import pandas as pd
import numpy as np

data = pd.read_csv('survey_responses.csv', index_col=0)
data.head(10)

#size is 1000 to get a dataset of that size 
def generate_new_data(data, size=1000):
    new_data = pd.DataFrame()
    
    #essentially mapping values here
    modify = {
    'Yes':'Strongly Agree',
    'Not Sure':'Agree',
    'Indifferent':'Disagree',
    'No':'Strongly Disagree'
    }
    
    modifying = data.replace(modify)

    for column in modifying.columns:
        amounts = modifying[column].value_counts(normalize=True, dropna=True)
        prob = 1 / len(amounts)
        # For assitance with using np.random.choice: https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html, Accessed 10 December, 2023.
        column_data = np.random.choice(amounts.index, size=size, p=amounts.fillna(prob))
        new_data[column] = column_data

    return new_data

new_data = generate_new_data(data, size=1000)
new_data.to_csv('generated-new.csv', index=False)

new_data.head(10)