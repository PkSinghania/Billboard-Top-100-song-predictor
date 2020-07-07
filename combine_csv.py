"""combining wo csv"""

import pandas as pd

df1 = pd.read_csv("out.csv")
df2 = pd.read_csv("pref.csv")

billboard_hits = df1[['Title','Artist','Featuring','duration_ms','acousticness','danceability','energy','instrumentalness','key','liveness','loudness','speechiness','tempo','valence','Hit']]
billboard_non_hits = df2[['Title','Artist','Featuring','duration_ms','acousticness','danceability','energy','instrumentalness','key','liveness','loudness','speechiness','tempo','valence','Hit']]

final_data = pd.concat([billboard_hits, billboard_non_hits], axis=0)

final_data.to_csv("final_data.csv", index = False)
