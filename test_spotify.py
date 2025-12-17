import spotipy
from spotipy.oauth2 import SpotifyOAuth

# 1. SETUP CREDENTIALS
# Replace these with your actual keys from the dashboard
CLIENT_ID = '5bc83e9abb1842b690f94c11d3eef335'
CLIENT_SECRET = '2a5ad0dfbe044cba93fb6a1cabf58853'
REDIRECT_URI = 'http://127.0.0.1:5000/callback'

# 2. AUTHENTICATION
# This will open a browser window asking you to login to Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID, 
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-library-read playlist-modify-public user-read-playback-state user-modify-playback-state"
))

# 3. TEST CONNECTION
print("Authentication successful!")
user = sp.current_user()
print(f"Logged in as: {user['display_name']}")

# 4. SEARCH FOR A SONG
print("Searching for a happy song...")
results = sp.search(q='Happy', limit=1, type='track')
track = results['tracks']['items'][0]
print(f"Found song: {track['name']} by {track['artists'][0]['name']}")