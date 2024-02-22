#!/Users/jack/opt/anaconda3/bin/python3

import os

REC_CITY = input('What is the most recent Non-US city you have visited? ')
FAV_MOVIE = input('What is your favorite movie? ')
UVA_YEAR = input('What year are you at UVA? ')

os.environ["REC_CITY"] = REC_CITY
os.environ["FAV_MOVIE"] = FAV_MOVIE
os.environ["UVA_YEAR"] = UVA_YEAR

print(os.getenv("REC_CITY"))
print(os.getenv("FAV_MOVIE"))
print(os.getenv("UVA_YEAR"))

