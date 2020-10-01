# Sentiment Analysis:
#   1) Tokenization: split a tweet up into subparts (words)
#   2) Bag of words model: count the # of times each word was mentioned
#   3) Look up the sentiment value of each word from a Sentiment lexicon to classify the 
#      whole sentiment value of the tweet

# Steps in the video I'm using as an example:
#   1) Register for the twitter API
#   2) Install dependencies
#   3) Write our script

# Dependencies:
# pip install tweepy
# pip install textblob

import tweepy
from textblob import TextBlob

# Variables for twitter authentication
consumer_key = 'XbRv8NaGUNLFMdLrYQihIPO0V'
consumer_secret = 'cTFYjEChVaMNo8uMfq7pZx6O8JQujdTDJrDrPq0xScsKlwnN83'
access_token = '873924627797393408-iH1UaVZMtBcHjTgQUmcIpfUwehsFs87'
access_token_secret = 'i0gooS78RQzOtkdojcuJf8p4oYvA0z69XoZKdmOpdI8QC'

# The act of authenticating (logging in) to twitter via tweepy
login = tweepy.OAuthHandler(consumer_key, consumer_secret)
login.set_access_token(access_token, access_token_secret)

# Create main variable
api = tweepy.API(login)

# Define what we are looking for
search = api.search('Trump')

# Define what to do with tweets that contain the search
for tweet in search:
    # make sure that it's printing the actual text of the tweet
    print(tweet.text)
    # create a variable to store the analysis of each tweet using TextBlob
    analyze = TextBlob(tweet.text)
    # print the sentiment value of each tweet:
    #   contains: polarity (positive or negative) & subjectivity (opinion vs facts)
    print(analyze.sentiment)