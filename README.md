# FinalYearProject

# Academic Title

Machine Learning-Based Assessment of Relationship Compatibility and Romantic Dealbreakers.

# Commercial Title

Early Days; Navigating Romantic Beginnings, One Question at a Time.

# Student Details

* Student Number: 20093135
* Name: Saoirse O'Donovan
* GitHub username: SaoirseODonovan

# Project Description

In an era of increasingly fast-paced dating dynamics, navigating the early stages of getting to know a potential partner has its complexities, particularly when it comes to assessing compatibility with those prospective individuals. Early Days’ overarching aim is to provide users with an application that aids them as they get to know a potential partner and to identify personal preferences. It does so by providing users with an engaging questionnaire that encapsulates a series of prompts to uncover what dealbreakers may exist for a particular individual to prevent them from entering a relationship. Once the user has completed the questionnaire, a machine learning technique, clustering, is utilised to categorise the user into a cluster group derived from the trends acknowledged in the responses they provided. The user may then progress and compare their responses to those of another user of their choice. A scoring algorithm will then supply users with a compatibility score, derived from the answers they gave. Early Days delivers this functionality through a stylistic interface to engage users and empower them to traverse the early relationship stages effectively.

# Project Landing Page

https://saoirseodonovan.github.io/fyp/

# Prerequisites

* Install Git
* Clone the repository
* Install Python

# Steps for set up (Windows)

``` pip install -r requirements.txt ```

``` python app.py ```

# How to use 

1.	Sign Up/Login
The user must begin by signing up to gain access to the site and the primary functionality or otherwise, login if they already have an account. Users can optionally set up two factor authentication also. 
 
2.	Explore the ‘welcome’ page
This is the initial screen presented to the users after signing in. It outlines the suggested steps to take for website use as well as detailing background information related to the website and its purpose. It also has a live feed of Early Days’ Instagram page.

3.	Take the Dealbreakers Quiz
There are numerous buttons on the ‘welcome’ page that direct the user to take the quiz as this step is the precursor to the rest of the developed features. This quiz contains a series of dealbreakers that may prevent someone from entering a relationship with a potential partner.

4.	Obtain your result 
The user then receives a ‘Lover Type’ category chosen for them using clustering, a machine learning technique, derived from their quiz answers. An email is also sent to the email entered by users during set up at this point with a copy of the results.

5.	Explore the ‘Profile Summary’ page 
This page presents users with graphs of the distribution of answers across all quiz questions so that users can see where their answers align or misalign with others. 

6.	Check your Compatibility
Users can then access the ‘Check Compatibility’  page, enter the username of another user that they’d like to assess their compatibility with and generate an overall compatibility score. They can then select a category out of four categories of values and preferences and generate a more detailed score. This score only considers a subset of the questions within the quiz to analyse user compatibility that is more specific. 

7.	Observe the other ‘Lover Types’ 
On the ‘Lover Types’ page, users can look at all the possible categories they could have been placed within during step 4. Each category is accompanied by a description of potential characteristics displayed by users who exist within this category.

8.	Log out 
If you’re all done, make sure to log out!


# References

* For assitance with elbow method and cost function: https://codinginfinite.com/elbow-method-in-python-for-k-means-and-k-modes-clustering/, https://codinginfinite.com/k-modes-clustering-for-categorical-data-in-python/, Accessed 15 January, 2024.
* For assitance with using np.random.choice: https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html, Accessed 10 December, 2023.
* For assistance with flask sign up, login and database (SQLAlchemy) usage: https://youtu.be/uZnp21fu8TQ?si=i165JQRHuDr-G8hO Accessed December 13, 2023.
* For assistance with is_authenticated() in base.html: https://www.freecodecamp.org/news/how-to-authenticate-users-in-flask/ Accessed December 14, 2023.
* For assistance with radio input type in survey.html: https://www.w3schools.com/tags/att_input_type_radio.asp Accessed December 17, 2023.
* Taggbox used for widget on welcome.html: https://taggbox.com/widget/ Accessed November 27, 2023.
* Font Awesome for icons: https://fontawesome.com/ Accessed November 28, 2023.
* Bootstrap for CSS in base.html: https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css Accessed November 22, 2023.
* For assistance with LabelEncoder usage: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html Accessed December 5, 2023.
* For assistance with KMeans clustering + resources gained from Data Mining module: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html Accessed December 2, 2023.
* For assistance with KModes usage: https://pypi.org/project/kmodes/ Accessed January 11, 2024.
* For assistance with .to_csv: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html Accessed January 19, 2024.
* For assistance with converting JSON formatted strings to lists: shttps://www.programiz.com/python-programming/json Accessed January 21, 2024.
* For assistance for zip() function: https://www.w3schools.com/python/ref_func_zip.asp Accessed January 22, 2024.
* For assistance with circle: https://stackoverflow.com/questions/4861224/how-to-use-css-to-surround-a-number-with-a-circle Accessed 22 January, 2024.
* For assistance with pd.melt: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html Accessed 25 January, 2024.
* For assistance with base64 encoding: https://www.geeksforgeeks.org/base64-b64encode-in-python/ Accessed 25 January, 2024.
* For assistance with displaying Base64 images in HTML: https://stackoverflow.com/questions/8499633/how-to-display-base64-images-in-html Accessed 25 January, 2024.
* For assistance and inspiration with footer: https://blog.stackfindover.com/responsive-html-footer-examples/#google_vignette Accessed 30 January, 2024.
* For lover type image generation: https://copilot.microsoft.com/images/create Prompt used for image generation: "9 different, modern symbols, no colour, to represent these nine different lover types: The Stringent Lover, The Adaptable Lover, The Balanced Lover, The Unbiased Lover, The Uniform Lover, The Neutral Lover, The Diverse Lover, The Flexible Lover, The Rigorous Lover." Accessed 27 January, 2024.
* For Bootstrap links and assitance with navigation bar toggle details: https://getbootstrap.com/docs/5.3/getting-started/introduction/ & https://getbootstrap.com/docs/5.0/components/navbar/ Accessed 02 February, 2024.
* To create the gifs on the welcome page I used a Canva template: Orange Black Modern Personal Branding Tips Animated Social Media Template by Daily Creative, Accessed 18 February, 2024.
* For assistance with setting up mail configurations: https://www.youtube.com/watch?v=nOkpTwPvDTg Accessed March 3, 2024.
* For assistance with boostrap grid structure to make the layout work on mobile also: https://getbootstrap.com/docs/4.0/layout/grid/, Accessed March 12, 2024.
* Couple images used on 'welcome' page are from the '[KR] Organic Lined Korean Daily Life' collection within the 'Elements': https://www.canva.com/, Accessed March 12, 2024.
* For assistance with short JQuery script for hiding flash messages on button click: https://stackoverflow.com/questions/25260841/close-a-window-with-javascript-onclick, Accessed March 13, 2024.
* For assistance with current_app usage: https://www.fullstackpython.com/flask-globals-current-app-examples.html Accessed March 16, 2024.
* For assistance with os.path options: https://docs.python.org/3/library/os.path.html Accessed March 16, 2024.
* For assistance with form container: https://w3codepen.com/html-css-login-form-page/ Accessed March 17, 2024.
* For the values infographic: https://codepen.io/MarkBoots/pen/Yzadapq Accessed March 18, 2024.
* Privacy policy example generated using ChatGPT 3.5 and modified to suit this application and the recorded data. Link to the ChatGPT 3.5 converstaion: https://chat.openai.com/share/652b7510-3474-4cd6-b634-7da163619f63 Accessed March 19, 2024.
* For assistance with use of app_context_processor: https://flask.palletsprojects.com/en/2.3.x/api/#flask.Blueprint.app_context_processor Accessed March 23, 2024.
* For assistance with key frames for banner loop animation: https://stackoverflow.com/questions/66618076/css-keyframe-translatex-and-rotatey-on-both-ends Accessed March 24, 2024.
* For 2fa assistance: https://youtu.be/o0XZZkI69E8?si=XWifHWK964C3rfWC Accessed March 29, 2024.

## Authors

- **Saoirse O'Donovan**

