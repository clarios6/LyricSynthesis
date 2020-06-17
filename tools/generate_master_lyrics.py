import os
from pathlib import Path
import glob
import sys
print(sys.getdefaultencoding())

basePath = Path(__file__).parent
lyricsPath = "../lyrics"
lyricType = "*.txt"
fullPath = (basePath / lyricsPath).resolve()

songs = glob.glob("../lyrics/*.txt")

with open("../lyrics/masterLyricFile.txt", encoding='utf-8', mode="w") as master:
    for song in songs:
        with open(song, encoding='utf-8', mode="r") as fp:
            master.write(fp.read())
