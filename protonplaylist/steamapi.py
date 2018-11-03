import requests

# figures out whether a URL is a vanity URL (https://steamcommunity.com/id/XXXXX),
# a regular profile URL (https://steamcommunity.com/profiles/XXXXXXXXXXXXXXXXX), or invalid
def getURLType(url):
    pass

# given a vanity url, returns the user ID
def resolveVanityURL(url):
    pass

# given a regular profile URL, returns the user ID
def getUserID(url):
    pass

# given a user ID, return a list of games they own
def getOwnedGames(userID):
    pass

# returns a list of games they have played in the last two weeks
def getGamesPlayedRecently(userID):
    pass

# given a list of game IDs, returns various infomration about the games
def getGameInformation(games):
    pass
