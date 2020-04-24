# Reddle
Prototype Reddit webscraper using the Praw and Pandas modules that scrapes authenticated users' saved posts into a collection table to be manipulated and sorted. Still a work in progress! Exports to csv file. 
Will need praw module and pandas installed. 
# How to install and use
First install packages and dependencies required using `pip install -r requirements`. Then, you will also need a developer account in Reddit to get the client tokens and keys needed to put into the main.py file to access your reddit profile and saved content. After that, run the program in `src` with `python3 main.py`, enter your username and password, and then your saved content will be in a `csv` file in the same folder as the Reddle folder. Voila!
