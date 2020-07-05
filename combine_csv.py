import pandas as pd

df1 = pd.read_csv("out.csv")
df2 = pd.read_csv("pref.csv")

df3 = df1[['Title','Artist','Featuring','duration_ms','acousticness','danceability','energy','instrumentalness','key','liveness','loudness','speechiness','tempo','valence','Hit']]
df4 = df2[['Title','Artist','Featuring','duration_ms','acousticness','danceability','energy','instrumentalness','key','liveness','loudness','speechiness','tempo','valence','Hit']]

df4 = pd.concat([df3, df4], axis=0)

df4.to_csv("final_data.csv", index = False)
