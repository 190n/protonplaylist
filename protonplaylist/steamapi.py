import requests
import re
from collections import namedtuple
from protonplaylist.secrets import steamAPIKey

reVanityURL = re.compile(r'^https?://steamcommunity\.com/id/(.*)$')
reProfileURL = re.compile(r'^https?://steamcommunity\.com/profiles/(.*)$')

# information about a game in a user's library
UserGame = namedtuple('UserGame', 'appID playtime playtimeTwoWeeks')

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
    apiCall += '&format=json'
    r = requests.get(apiCall)
    if r.status_code != 200:
        raise Exception('HTTP error {} from Steam API'.format(r.status_code))
    json = r.json()['response']
    if json['success'] != 1:
        raise Exception('Steam API error: {}'.format(json['message']))
    return json['steamid']

# given a regular profile URL, returns the user ID
def getUserID(url):
    try:
        return reProfileURL.findall(url)[0]
    except IndexError:
        raise Exception('Invalid URL or not a profile URL: {}'.format(url))

# given a dictionary representing a game from getOwnedGames, returns the same information as a UserGame
def createUserGame(game):
    # if the Steam API doesn't include playtime_2weeks, the game has not been launched in 2 weeks so the playtime is zero
    playtimeTwoWeeks = game['playtime_2weeks'] if 'playtime_2weeks' in game else 0
    return UserGame(game['appid'], game['playtime_forever'], playtimeTwoWeeks)

# given a user ID, return a list of games they own
def getOwnedGames(userID):
    apiCall = 'https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/'
    apiCall += '?key=' + steamAPIKey
    apiCall += '&steamid=' + userID
    apiCall += '&format=json'
    r = requests.get(apiCall)
    if r.status_code != 200:
        raise Exception('HTTP error {} from Steam API'.format(r.status_code))
    json = r.json()['response']
    if json == {}:
        raise Exception('Could not get game list')
    return [createUserGame(g) for g in json['games']]

# given a list of game IDs, returns various infomration about the games
def getGameInformation(games):
    pass
