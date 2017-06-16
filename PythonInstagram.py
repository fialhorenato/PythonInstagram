import urllib2
import json

class Instagram:

    def __init__(self, access_token):
        self.access_token = access_token
    
    def _getDictionary(self,url):
        try:
            return json.loads(urllib2.urlopen(url).read())
        except urllib2.HTTPError as e:
            return json.loads(e.read())

    def getLastMediaLiked(self):
        url = "https://api.instagram.com/v1/users/self/media/liked?access_token=" + self.access_token
        response = self._getDictionary(url)
        return response

    def getUserID(self,username):
        url = "https://api.instagram.com/v1/users/search?q=" + username + "&access_token=" + self.access_token
        response = self._getDictionary(url)
        return response

    def getMyProfileInfo(self):
        url = "https://api.instagram.com/v1/users/self/?access_token=" + self.access_token
        response = self._getDictionary(url)
        return response

    def getMyMostRecentMedia(self):
        url = "https://api.instagram.com/v1/users/self/media/recent/?count=1&access_token=" + self.access_token
        response = self._getDictionary(url)
        return response

    def getProfileInfo(self,user_id):
        url = "https://api.instagram.com/v1/users/" + user_id + "/?access_token=" + self.access_token
        response = self._getDictionary(url)
        return response
    
    def getMyFollowers(self):
        return self.getMyProfileInfo()['data']['counts']['followed_by']