
import praw
import pandas as pd

usernamed = input("What's your username? ")
passwrd = input("What's your password? ")

reddit = praw.Reddit(client_id='', \
                    client_secret='', \
                    user_agent='', \
                    username=usernamed, \
                    password=passwrd)

savedpostsdict = {"saved content url":[], \
                  "saved content title":[]}

savedcommentsdict = {"saved comments": []}


savedcontent = reddit.user.me().saved(limit=None)

for submission in savedcontent:
    if isinstance(submission, praw.models.Comment):
        savedcommentsdict["saved comments"].append(submission.body)
    elif isinstance(submission, praw.models.Submission):
        savedpostsdict["saved content url"].append(submission.url)
        savedpostsdict["saved content title"].append(submission.title)


present_posts_data = pd.DataFrame(savedpostsdict)
present_comments_data = pd.DataFrame(savedcommentsdict)
present_posts_data.to_csv('savedredditposts.csv', index=True)
present_comments_data.to_csv('savedredditcomments.csv', index=True)
