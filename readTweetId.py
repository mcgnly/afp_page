def readTweetId():
    #I only care about tweets I haven't seen yet
    #read the last tweet ID from the file holding it
    #for testing purposes, a few tweets ago is 681658764840140800
    with open('lastTweetId.txt', 'r') as f:
        readData = f.read()
        return readData
    f.closed