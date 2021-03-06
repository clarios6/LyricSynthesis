import os
import requests
import urllib.request
import json
import csv
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from pathlib import Path


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
lyrics = []
for i, x in enumerate(songListURLs):
    url = URL_SITE +  x
    page = requests.get(url)
    html = BeautifulSoup(page.text, "html.parser")
    songLyrics = html.find("div", class_="lyrics").get_text()
    lyrics.append({'id': i, 'name': x, 'lyrics': songLyrics})

### Lyric Saving ###
basePath = Path(__file__).parent

fileName = artist + ".json"
dirNameJSON = "../lyrics/" + artist + ".json"
filePath = (basePath / dirNameJSON).resolve()
with open(filePath, encoding='utf-8', mode='w') as fp:
    json.dump(lyrics, fp, indent=4)

csvFile = artist + ".csv"
dirNameCSV = "../lyrics/" + artist + ".csv"
csvColumns = ["id", "name", "lyrics"]
filePath = (basePath / dirNameCSV).resolve()
with open(filePath, encoding='utf-8', mode='w') as fp:
    writer = csv.DictWriter(fp, fieldnames=csvColumns)
    writer.writeheader()
    for x in lyrics:
        writer.writerow(x)

txtFile = artist + ".txt"
dirNameTXT = "../lyrics/" + artist + ".txt"
filePath = (basePath / dirNameTXT).resolve()
with open(filePath, encoding='utf-8', mode='w') as fp:
    for x in lyrics:
        fp.write("Title:" + x['name'] + "\n")
        fp.write(x['lyrics'] + "\n")
