import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = '40d25bb4dc924f7791d818887e50183d'
CLIENT_SECRET = 'b8aede48580f47409f9c630ef366e914'

def get_client_cred():
    
    client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_song_id(artistName, trackName, sp):
    q = "artist:{} track:{}".format(artistName, trackName)
    song_id = 0
    song = sp.search(q=q, type="track", limit=1)

    for i, t in enumerate(song['tracks']['items']):
        song_id = t['id']

    return song_id

def get_audio_features(track_id, sp):
    
    obj = None
    if track_id:

        features = sp.audio_features(str(track_id))
        if features[0]:

            duration_ms = features[0]['duration_ms']
            key = features[0]['key']
            acousticness = features[0]['acousticness']
            danceability = features[0]['danceability']
            energy = features[0]['energy']
            instrumentalness = features[0]['instrumentalness']
            liveness = features[0]['liveness']
            loudness = features[0]['loudness']
            speechiness = features[0]['speechiness']
            tempo = features[0]['tempo']
            valence = features[0]['valence']

            obj = {
                "duration_ms": duration_ms,
                "key": key,
                "acousticness": acousticness,
                "danceability": danceability,
                "energy": energy,
                "instrumentalness": instrumentalness,
                "liveness": liveness,
                "loudness": loudness,
                "speechiness": speechiness,
                "tempo": tempo,
                "valence": valence
            }

        return obj if obj else None



