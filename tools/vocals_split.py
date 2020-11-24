from spleeter.separator import Separator
import os
from pathlib import Path
import glob
import sys

basePath = Path(__file__).parent
songsPath = "../songs/*.wav"
outputPath = "../output"
songsPath = (basePath / songsPath).resolve()
outputPath = (basePath / outputPath).resolve()

songs = glob.glob(str(songsPath))

outputPath = str(outputPath)
separator = Separator('spleeter:5stems')
for song in songs:
    separator.separate_to_file(song, outputPath, codec='mp3')
