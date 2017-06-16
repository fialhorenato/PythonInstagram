from PythonInstagram import Instagram
import os

IG = Instagram(os.environ['ACCESS_TOKEN'])

# GET HOW MANY FOLLOWERS THE OWNER OF THE ACCESS TOKEN HAVE
print IG.getMyFollowers()

# GET THE LAST MEDIA THAT THE OWNER OF THE ACCESS TOKEN LIKED
print IG.getLastMediaLiked()

# GET THE PROFILE INFO FOR THE OWNER OF THE ACCESS TOKEN
print IG.getMyProfileInfo()

# GET THE PROFILE INFO FOR ANY PUBLIC USER, GETS AN ID AS PARAMETER
id = IG.getMyProfileInfo()['data']['id']
print IG.getProfileInfo(id)