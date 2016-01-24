def saveTweetId(tweetId):
    #update what was the last tweet I looked at
    #save this number to a file

        value = (tweetId)
        s = str(value)
        with open('lastTweetId.txt', 'w') as f:
            f.write(s)
        f.closed