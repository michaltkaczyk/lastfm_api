import requests

user = open("credentials/lastfm_user.txt").read()
api_key = open("credentials/lastfm_key.txt").read()

path = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=" + user + "&api_key=" + api_key + \
       "&format=json"

response = requests.get(path)
print(response.status_code)

