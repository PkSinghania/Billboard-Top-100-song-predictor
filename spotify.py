from get_feature import get_client_cred, get_song_id, get_audio_features
from threading import Thread
import pandas as pd
import spotipy
from requests.exceptions import ConnectionError
import requests
import time

thing = [[] for i in range(8)]
logg = [0 for i in range(8)]

def write_log():
    print(sum(logg))
    
def extract_feature(x, i):

    cred = get_client_cred()
    song_artist = x['Artist']
    song_title = x['Title']
    song_artist = song_artist.split("Featuring")[0]
    song_artist = song_artist.split("&")[0]
    obj = None
    try:
        song_id = get_song_id(song_artist, song_title, cred)
        obj = get_audio_features(song_id, cred)
    except requests.exceptions.RequestException as e:    # This is the correct syntax
        print(e)

    if obj:
        x['duration_ms'] = obj['duration_ms']
        x['key'] = obj['key']
        x['acousticness'] = obj['acousticness']
        x['danceability'] = obj['danceability']
        x['energy'] = obj['energy']
        x['instrumentalness'] = obj['instrumentalness']
        x['liveness'] = obj['liveness']
        x['loudness'] = obj['loudness']
        x['speechiness'] = obj['speechiness']
        x['tempo'] = obj['tempo']
        x['valence'] = obj['valence']
        thing[i].append(x)


def feat_util(df, i):
    for y,x in df.iterrows():
        extract_feature(x, i)
        logg[i]+=1

def multi_thread(df):
    print("{} to be done" .format(len(df)))
    arr = [df[i::8] for i in range(8)]
    c = len(arr[7])
    threads = []
    j = 0
    for i in range(8):
        p = Thread(target = feat_util, args = (arr[i], i))
        p.start()
        threads.append(p)

    while(logg[7] < c):
        q = Thread(target = write_log, args = ())
        q.start()
        time.sleep(5)
        q.join()
        
    for i in threads:
        i.join()


df = pd.read_csv("billboard_top_100.csv")
df2 = pd.DataFrame(columns = ['Title'])
multi_thread(df)
for i in range(8):
    for j in thing[i]:
        df2 = df2.append(j)
df2.to_csv("pref.csv")
