import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random

# 1) Set Up
CLIENT_ID = '5bc83e9abb1842b690f94c11d3eef335'
CLIENT_SECRET = '2a5ad0dfbe044cba93fb6a1cabf58853'
REDIRECT_URI = 'http://127.0.0.1:5000/callback'

# Page Config
st.set_page_config(page_title="Mood Music Player", page_icon="🎵")
st.title("🎵 Mood Music Player")
st.write("Take a selfie, and I'll play the perfect song for your mood.")

# 2) Load Models
@st.cache_resource
def load_models():
    # Load Emotion Model
    emotion_model = load_model('emotion_model.hdf5', compile=False)
    # Load Face Detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    return emotion_model, face_cascade

try:
    emotion_classifier, face_classifier = load_models()
    emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
    st.success("✅ AI System Ready")
except:
    st.error("❌ Error: Could not load 'emotion_model.hdf5'. Check your folder.")

# Spotify Setup
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-library-read"
))

# 3) Music Logic
def get_music_link(mood):
    search_query = ""
    if mood == 'Happy':
        search_query = "Happy Upbeat Pop"
    elif mood == 'Sad':
        search_query = "Sad Piano Acoustic" 
    elif mood == 'Angry':
        search_query = "Heavy Metal Rock"
    elif mood == 'Neutral' or mood == 'Fear':
        search_query = "Lofi Chill Beats"
    elif mood == 'Surprise':
        search_query = "High Energy EDM"
    else:
        search_query = "Top Hits"

    try:
        # Randomized Search to avoid same songs
        random_offset = random.randint(0, 10)
        # We keep market='IN' just to ensure songs are playable in India
        results = sp.search(q=search_query, limit=10, offset=random_offset, type='track', market='IN')
        
        if results and results['tracks']['items']:
            item = random.choice(results['tracks']['items'])
            track_name = item['name']
            artist = item['artists'][0]['name']
            url = item['external_urls']['spotify']
            return track_name, artist, url
    except Exception as e:
        st.error(f"Spotify Error: {e}")
    
    return None, None, None

# 4) App Interface
img_file_buffer = st.camera_input("Take a Picture")

if img_file_buffer is not None:
    # Convert photo to format AI understands
    file_bytes = np.asarray(bytearray(img_file_buffer.read()), dtype=np.uint8)
    frame = cv2.imdecode(file_bytes, 1)
    
    # Process Image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 1.1 = Scan more detailed (slower but catches more faces)
    # 4 = Less strict about what counts as a face
    faces = face_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    if len(faces) > 0:
        for (x, y, w, h) in faces:
            # Crop Face
            roi_gray = gray[y:y+h, x:x+w]
            roi_gray = cv2.resize(roi_gray, (64, 64))
            roi = roi_gray.astype('float') / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)

            # Predict Mood
            prediction = emotion_classifier.predict(roi, verbose=0)[0]
            label = emotion_labels[prediction.argmax()]
            
            # Show Result
            st.header(f"You look... **{label}**")
            
            # Get Song
            track, artist, link = get_music_link(label)
            
            if track:
                st.subheader(f"🎶 Recommended: {track}")
                st.write(f"by {artist}")
                # Clickable Button
                st.link_button("▶️ Play on Spotify", link)
            else:
                st.write("Could not find a song.")
            
            # Draw box on face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            st.image(frame, channels="BGR")
            break
    else:

        st.warning("No face detected! Try moving closer.")
