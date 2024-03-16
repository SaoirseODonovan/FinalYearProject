import base64
import io
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from .utilities import loopQuestions
from flask import current_app
import os

#changed code to simply save the images to the file system instead of using buffer as bottleneck caused 

def graph(data, questions):
    # For assistance with os.path options: https://docs.python.org/3/library/os.path.html Accessed March 16, 2024.
    #dir of images
    # For assistance with current_app usage: https://www.fullstackpython.com/flask-globals-current-app-examples.html Accessed March 16, 2024.
    save_images_location = os.path.normpath(os.path.join(current_app.static_folder, "images"))
    #24 images, 0-23
    files_exist = []

    for i in range(24):
        if os.path.exists(os.path.join(save_images_location, f"graph{i}.png")):
            files_exist.append(True)
            print(files_exist)
        else:
            files_exist.append(False)
            print(files_exist)

    if not False in files_exist:
        #all files are in the specified location
        images = []
        #'rb' - read binary
        for i in range(24):
            with open(os.path.join(save_images_location, f"graph{i}.png"), 'rb') as file:

                transformed_image = base64.b64encode(file.read()).decode('utf-8')

                images.append(transformed_image)

        return images
    else:
        #certain files or all files don't exist 
        # For assistance with pd.melt: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html Accessed 25 January, 2024.
        #convert df so it can be used for graphing (seaborn)
        melt_df = pd.melt(data, value_vars=questions, var_name="Question", value_name="Answer")
        #will hold base64 formatted images
        images = []

        for i, question in enumerate(questions):

            colours = {'Strongly Agree': '#660000',
                    'Agree': '#EDB6C0',
                    'Disagree': '#7DAC9B',
                    'Strongly Disagree': '#283D2A'}

            plt.figure(figsize=(9, 7))
            #hue option added to remove warning in console
            sns.countplot(x="Answer", data=melt_df[melt_df["Question"] == question], order=['Strongly Agree', 'Agree', 'Disagree', 'Strongly Disagree'], palette=colours, hue=None)
            plt.title(f"{loopQuestions[i]}", fontsize=13)
            plt.xlabel('Answer Options')
            plt.ylabel('Answer Popularity')
            #remove them
            plt.yticks([])
            #save new images again
            save_path = os.path.join(save_images_location, f"graph{i}.png")
            plt.savefig(save_path)
            plt.close()

            with open(save_path, 'rb') as file:
                # For assistance with base64 encoding: https://www.geeksforgeeks.org/base64-b64encode-in-python/ Accessed 25 January, 2024.
                transformed_image = base64.b64encode(file.read()).decode('utf-8')

            images.append(transformed_image)

        return images