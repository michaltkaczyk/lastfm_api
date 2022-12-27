import requests

user = open("credentials/lastfm_user.txt").read()
api_key = open("credentials/lastfm_key.txt").read()

LFM_API_ROOT = "http://ws.audioscrobbler.com/2.0/"

lfm_api_path = LFM_API_ROOT +\
               "?method=user.getrecenttracks&user=" + user +\
               "&api_key=" + api_key +\
               "&format=json"

response = requests.get(lfm_api_path)
print(response.status_code)

results = response.json()['recenttracks']['track']

tracks_list = []

for scrobbled_item in results:

    # Skip currently playing track
    if '@attr' in scrobbled_item:
        if 'nowplaying' in scrobbled_item['@attr']:
            if scrobbled_item['@attr']['nowplaying'] == "true":
                continue

    tracks_list.append(
        [scrobbled_item['artist']['#text'],
         scrobbled_item['album']['#text'],
         scrobbled_item['name'],
         scrobbled_item['date']['#text']])

print(tracks_list)
