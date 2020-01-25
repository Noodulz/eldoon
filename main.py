# Will be using praw modules. And pandas to format the scraped data to port to .csv file
import praw
import pandas as pd

# Ask for user authentication first
usernamed = input("What's your username? ")
passwrd = input("What's your password? ")

# User will need to create an app in reddit and put in the id and secret tokens to use this
reddit = praw.Reddit(client_id='', \
                    client_secret='', \
                    user_agent='', \
                    username=usernamed, \
                    password=passwrd)

# Created two dictionaries to store the saved content. One for posts and one for comments since they can't mingle
savedpostsdict = {"saved content url":[], \
                  "saved content title":[]}

savedcommentsdict = {"saved comments": []}

# Scrapes all of the user's own content
savedcontent = reddit.user.me().saved(limit=None)

# Checks each saved content to see if it is a comment or submitted post instance and appends to respective dictionaries
for submission in savedcontent:
    if isinstance(submission, praw.models.Comment):
        savedcommentsdict["saved comments"].append(submission.body)
    elif isinstance(submission, praw.models.Submission):
        savedpostsdict["saved content url"].append(submission.url)
        savedpostsdict["saved content title"].append(submission.title)

# Formats dictonaries with scraped data accordingly with Pandas
present_posts_data = pd.DataFrame(savedpostsdict)
present_comments_data = pd.DataFrame(savedcommentsdict)

# Ports each dictionary to a .csv file and numbers them in order. .csv files should be in the same folder as this main.py script
present_posts_data.to_csv('savedredditposts.csv', index=True)
present_comments_data.to_csv('savedredditcomments.csv', index=True)
