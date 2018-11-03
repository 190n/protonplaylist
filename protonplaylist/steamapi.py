import requests
import re
from protonplaylist.secrets import steamAPIKey

reVanityURL = re.compile(r'^https?://steamcommunity\.com/id/(.*)$')
reProfileURL = re.compile(r'^https?://steamcommunity\.com/profiles/(.*)$')

def isURLValid(url):
    if reVanityURL.match(url):
        return True
    elif reProfileURL.match(url):
        return True
    return False

def isVanityURL(url):
    if reVanityURL.match(url):
        return True
    return False

# given a vanity url, returns the user ID
def resolveVanityURL(url):
    try:
        vanityURL = reVanityURL.findall(url)[0]
    except IndexError:
        raise Exception('Not a vanity URL: {}'.format(url))

    apiCall = 'https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/'
    apiCall += '?key=' + steamAPIKey
    apiCall += '&vanityurl=' + vanityURL
    r = requests.get(apiCall)
    json = r.json()['response']
    if json['success'] != 1:
        raise Exception('Steam API error: {}'.format(json['message']))
    return json['steamid']

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
