import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials # UPDATED IMPORT
import random

# =========================================================================
# 1. SETUP & CONFIGURATION
# =========================================================================
CLIENT_ID = '5bc83e9abb1842b690f94c11d3eef335'
CLIENT_SECRET = '2a5ad0dfbe044cba93fb6a1cabf58853'

# Page Config
st.set_page_config(page_title="Mood Music Player", page_icon="🎵")
st.title("🎵 Mood Music Player")
st.write("Take a selfie, and I'll play the perfect song for your mood.")

# =========================================================================
# 2. LOAD MODELS (Cached for Speed)
# =========================================================================
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
except Exception as e:
    st.error(f"❌ Error loading models: {e}. Check if 'emotion_model.hdf5' is uploaded.")

# =========================================================================
# 3. SPOTIFY SETUP (NO LOGIN REQUIRED)
# =========================================================================
# This method prevents the "[Errno 98] Address already in use" error
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# =========================================================================
# 4. MUSIC LOGIC (INTERNATIONAL)
# =========================================================================
def get_music_link(mood):
    # Standard International Genres
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
        # Randomized Search to keep it fresh
        random_offset = random.randint(0, 10)
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

# =========================================================================
# 5. APP INTERFACE (CAMERA)
# =========================================================================
img_file_buffer = st.camera_input("Take a Picture")

if img_file_buffer is not None:
    # Convert photo to format AI understands
    file_bytes = np.asarray(bytearray(img_file_buffer.read()), dtype=np.uint8)
    frame = cv2.imdecode(file_bytes, 1)
    
    # Process Image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # DEBUG: Show what the AI sees (Helps check lighting)
    with st.expander("See what the AI sees (Debug)"):
        st.image(gray, caption="Grayscale Input")

    # Detect Faces (Adjusted for better sensitivity)
    # scaleFactor 1.1 = Scan slower but find more faces
    # minNeighbors 4 = Slightly less strict
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
                st.link_button("▶️ Play on Spotify", link)
            else:
                st.write("Could not find a song.")
            
            # Draw box on face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            st.image(frame, channels="BGR", caption="Analyzed Face")
            break
    else:
        st.warning("No face detected! Try moving closer to the camera or turning on a light.")
