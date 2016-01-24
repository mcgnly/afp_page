# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from mailgun import mailgun
from saveTweetId import saveTweetId
from readTweetId import readTweetId

#todo:
    #add email addresses to database? dictionary?
    #match the list of emails to a keyword or DB entry or something
    #be able to add an email to this list
    #be able to add a keyword to this dictionary/DB
    #be able to remove email address
    #get a better/bigger soln than mailgun?
    #django website?




#open a file called "apikeys" with keys and tokens for Twitter separated by newlines,
# strip the invisible newline char from it
with open('apikeys.txt', 'r') as keyFile:
    keyFile = open('apikeys.txt', 'r')
    ACCESS_TOKEN = keyFile.readline().rstrip()
    ACCESS_TOKEN_SECRET = keyFile.readline().rstrip()
    CONSUMER_KEY = keyFile.readline().rstrip()
    CONSUMER_SECRET = keyFile.readline().rstrip()
    MAILGUN_KEY = keyFile.readline().rstrip()
keyFile.closed

oauth = OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter REST API
twitter = Twitter(auth=oauth)

#this is the text I'm looking for in the tweets
importantWord = "berlin"

#read the ID of the last tweet I've already seen is so I can look for only new ones
readData = int(readTweetId())

# Get a particular user's timeline (up to 3,200 of his/her most recent tweets).
# this is for amanda palmer, since I last looked at it, excluding replies and retweets
lastTweets = twitter.statuses.user_timeline.tweets(screen_name="amandapalmer", since_id = readData,
                                                   exclude_replies = "true", include_rts = "false")

#get the last tweet's ID and save it out to a file so I only start looking from there
if len(lastTweets)>0:
    saveTweetId(lastTweets[0]['id'])

#step through list of last tweets
for i in lastTweets:
    #strip the text out of the json of the tweet
    thisTweet = i['text']

    #look for the trigger word
    if importantWord in thisTweet.lower():
        #trigger an email with the full text of the tweet
        mailgun(MAILGUN_KEY, thisTweet)

