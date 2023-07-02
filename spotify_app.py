import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id  = '2e1b2981b57846dc9c2c496d9bdec4f7'
client_secret = 'c14fc233d6ec4a46becb90bae7adeaf7'
redirect_uri = 'https://open.spotify.com/'

#create an instance of the spotify client
auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='user-modify-playback-state')
sp = spotipy.Spotify(auth_manager=auth_manager)

# Play a song
sp = spotipy.Spotify(auth_manager=auth_manager)


track_uri = 'https://open.spotify.com/track/328AFGrVD07umdLdeoTK25?si=8c022dad7b514098'  
sp.start_playback(uris=[track_uri])
