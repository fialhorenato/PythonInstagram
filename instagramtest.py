import urllib2
import os
import json

access_token = os.environ['ACCESS_TOKEN']

def getJSON(url):
    try:
        return json.loads(urllib2.urlopen(url).read())
    except urllib2.HTTPError as e:
        return json.loads(e.read())

def getLastMediaLiked():
    url = "https://api.instagram.com/v1/users/self/media/liked?access_token=" + access_token
    response = getJSON(url)
    return response

def getUserID(username):
    url = "https://api.instagram.com/v1/users/search?q=" + username + "&access_token=" + access_token
    response = getJSON(url)
    return response

def getMyInfo():
    url = "https://api.instagram.com/v1/users/self/?access_token=" + access_token
    response = getJSON(url)
    return response

def getMyMostRecentMedia():
    url = "https://api.instagram.com/v1/users/self/media/recent/?count=1&access_token=" + access_token
    response = getJSON(url)
    return response

def getProfileInfo(user_id):
    url = "https://api.instagram.com/v1/users/" + user_id + "/?access_token=" + access_token
    response = getJSON(url)
    return response