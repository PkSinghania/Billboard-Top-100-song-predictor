""" get lyrics of the song using genius api. We are using multithreading to make it fast"""

import lyricsgenius
import pandas as pd
import time
from threading import Thread

df = pd.read_csv("final_data.csv")
genius = lyricsgenius.Genius("Your code")
df2 = pd.DataFrame( columns = ['song', 'artist', 'text'] )

thing = [[] for i in range(50)]

def improve_lyrics(a):
    
    a = a.replace("F**k", "Fuck")
    a = a.replace("B****", "Bitch")
    a = a.replace("S**t", "Shit")
    a = a.replace("P****", "Pussy")
    a = a.replace("F*****g", "Fucking")
    a = a.replace("F***", "Fuck")
    return a

def get_lyrics(j, i):
    try:
        a = genius.search_song(j['Title'], j['Artist'] )
        if(a):
            j['lyrics'] = improve_lyrics(a.lyrics)
            thing[i].append(j)
    except TimeoutError as e:
        print(e)
    except:
        pass


def feat_util(df, i):
    for x,j in df.iterrows():
        get_lyrics( j, i )
        

def multi_thread(df):
    
    arr = [df[i::40] for i in range(40)]
    threads = []
    for i in range(40):
        p = Thread(target = feat_util, args = (arr[i], i))
        p.start()
        threads.append(p)

        
    for i in threads:
        i.join()


multi_thread(df)
for i in range(50):
    for j in thing[i]:
        df2 = df2.append(j)
df2.to_csv("done2.csv")
