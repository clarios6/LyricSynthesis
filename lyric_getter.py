import os
import requests
import urllib
from dotenv import load_dotenv

# load_dotenv()

URL_API = "https://api.genius.com/"
URL_SEARCH = "search?q="

ACCESS_TOKEN = os.getenv('GENIUS_CLIENT_ACCESS_TOKEN')

artist = input("Enter artist name:\n")

# Generating Query
query = URL_API + URL_SEARCH + urllib.quote(artist)
request = urllib.Request(query)
request.add_header("Authorization", "Bearer" + ACCESS_TOKEN)
request.add_header("User-Agent", "")

response = urllib.urlopen(request, timeout=3)
json_obj = response.json()
json_obj.viewkeys()
