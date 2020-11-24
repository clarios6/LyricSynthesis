import os
from pathlib import Path
import glob
import sys
print(sys.getdefaultencoding())

basePath = Path(__file__).parent
lyricsPath = "../lyrics"
lyricType = "*.txt"
masterFile = "masterLyricFile.txt"
songsPath = (basePath / lyricsPath / lyricType).resolve()
masterPath = (basePath / lyricsPath / masterFile).resolve()

songs = glob.glob(str(songsPath))

with open(masterPath, encoding='utf-8', mode="w") as master:
    for song in songs:
        with open(song, encoding='utf-8', mode="r") as fp:
            master.write(fp.read())
