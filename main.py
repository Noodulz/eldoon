# Still a work in progress to be able to scrape both saved posts and saved comments!!! Ahhh

import praw
import pandas as pd
import datetime as dt

usernamed = input("What's your username? ")
passwrd = input("What's your password? ")

reddit = praw.Reddit(client_id='2B8S712oxagcyA', \
                    client_secret='qMSvKvrCYuJNsaPoRmZxrcoY-mk', \
                    user_agent='Eldoon', \
                    username=usernamed, \
                    password=passwrd)

savedpostsdict = {"saved title":[], \
            "url":[]}
savedcommentsdict = {"saved comments":[]}

savedposts = reddit.user.me().submissions.new(limit=None)
savedcomments = reddit.redditor(usernamed).saved(limit=5)

for submission in savedposts:
    savedpostsdict["url"].append(submission.url)
    savedpostsdict["saved title"].append(submission.title)

for submission in savedcomments:
    savedcommentsdict["saved comments"].append(submission.body)

present_posts_data = pd.DataFrame(savedpostsdict)
present_comments_data = pd.DataFrame(savedcommentsdict)
present_posts_data.to_csv('savedredditposts.csv', index=False)
present_comments_data.to_csv('savedcomments.csv', index=False)
