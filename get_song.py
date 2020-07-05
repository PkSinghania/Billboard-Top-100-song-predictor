import billboard
from datetime import datetime, timedelta 
import re
import pandas as pd
import matplotlib.pyplot as plt

START_DATE = '2000-01-01'
END_DATE = '2018-01-01'
CHART = 'hot-100'

def tracks_generator():
    
    curr_date = START_DATE
    song_tracks = list()

    while(curr_date < END_DATE):
        chart = billboard.ChartData(CHART, date=curr_date, timeout=900)

        for tracks in chart:
            song_tracks.append( [ 1, tracks.title, tracks.artist ] )
            #print(tracks.title + " " + tracks.artist)
        next_date = str( datetime.strptime(curr_date, '%Y-%m-%d') + timedelta(7) )
        regex = r"([0-9]{4})-([0-9]{2})-([0-9]{2})"
        arr = re.findall(regex, next_date)
        curr_date = '-'.join(arr[0])
        print(curr_date)
        
    return song_tracks

def featuring(artist):

    if "Featuring" in artist :
        return 1
    else :
        return 0


def prepare_data(songs):

    df = pd.DataFrame(songs)
    df.columns=["Hit", "Title", "Artist"]
    df = df.drop_duplicates(subset=["Title", "Artist"], keep="first")
    df["Featuring"] = df.apply(lambda row: featuring(row['Artist']), axis=1)
    return df

songs = tracks_generator()
df = prepare_data(songs)
df.to_csv("billboard_top_100.csv")
