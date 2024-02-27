import base64
import io
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def graph(data, questions):
    # For assistance with pd.melt: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html Accessed 25 January, 2024.
    #convert df so it can be used for graphing (seaborn)
    melt_df = pd.melt(data, value_vars=questions, var_name="Question", value_name="Answer")
    #will hold base64 formatted images
    images = []

    for question in questions:
        #for storing the images in memory
        buffer = io.BytesIO()

        plt.figure(figsize=(9, 7))
        sns.countplot(x="Answer", data=melt_df[melt_df["Question"] == question], order=['Strongly Agree', 'Agree', 'Disagree', 'Strongly Disagree'], palette="ch:s=-.2,r=.6")
        plt.title(f"{question}", fontsize=7)
        plt.xlabel('Answer Options')
        plt.ylabel('Answer Popularity')
        #remove them
        plt.yticks([])
        #save as PNG in binary stream 
        plt.savefig(buffer, format='png')
        #get the first image in binary stream
        buffer.seek(0)
        # For assistance with base64 encoding: https://www.geeksforgeeks.org/base64-b64encode-in-python/ Accessed 25 January, 2024.
        #encoding to embed in HTML
        transformed_image = base64.b64encode(buffer.read()).decode('utf-8')
        #mem management
        buffer.close()

        images.append(transformed_image)

    return images