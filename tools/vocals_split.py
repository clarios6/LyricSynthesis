from spleeter.separator import Separator
import os
from pathlib import Path
import glob
import sys

basePath = Path(__file__).parent
songsPath = "../songs/*.mp3"
outputPath = "../output"
songsPath = (basePath / songsPath).resolve()
outputPath = (basePath / outputPath).resolve()

songs = glob.glob(str(songsPath))

outputPath = str(outputPath)
separator = Separator('spleeter:2stems')
for song in songs:
    separator.separate_to_file(song, outputPath, codec='mp3')
