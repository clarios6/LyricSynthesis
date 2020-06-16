import os
import requests
import urllib.request
import json
from dotenv import load_dotenv
from bs4 import BeautifulSoup


# Setting up Environment
URL_API = "https://api.genius.com/"
URL_SITE = "https://genius.com" # Note the API returns with a / so we don't add it here!
URL_SEARCH = "search?q="
URL_ARTIST = "artists/"
URL_SONGS = "/songs"
URL_PAGE = "?page="

load_dotenv()
ACCESS_TOKEN = os.getenv("GENIUS_CLIENT_ACCESS_TOKEN")

artist = input("Enter artist name:\n")
artist = "Modern Baseball"

print(artist)

# Generating Query
query = URL_API + URL_SEARCH + artist
headers = { "Authorization": "Bearer " + ACCESS_TOKEN}

# Sending Query
response = requests.get(query, headers=headers)
data = response.json()
songListURLs = []
if artist == data['response']['hits'][0]['result']['primary_artist']['name']:
    artistID = data['response']['hits'][0]['result']['primary_artist']['id']
    query = URL_API + URL_ARTIST + str(artistID) + URL_SONGS
    response = requests.get(query, headers=headers)
    data = response.json()
    #Only gets up to the first twenty songs for now
    page = 2
    for x in data['response']['songs']:
        songListURLs.append(x['path'])
    while data['response']['next_page'] != None:
        query = URL_API + URL_ARTIST + str(artistID) + URL_SONGS + URL_PAGE + str(page)
        response = requests.get(query, headers=headers)
        data = response.json()
        for x in data['response']['songs']:
            songListURLs.append(x['path'])
        page += 1
else:
    print("Error with artist name, double check spelling")

### Lyric Scraping ###
lyrics = {}
for x in songListURLs:
    url = URL_SITE +  x
    page = requests.get(url)
    html = BeautifulSoup(page.text, "html.parser")
    songLyrics = html.find("div", class_="lyrics").get_text()
    lyrics[x] = songLyrics

### Lyric Saving ###
fileName = artist + ".json"
with open("../lyrics/" + fileName, 'w') as fp:
    json.dump(lyrics, fp, indent=4)
