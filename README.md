## AI Mood Music Player

A smart AI-powered web application that detects your current emotion from your facial expression and recommends the perfect Spotify song to match your mood.

Built with **Python**, **Streamlit**, **Computer Vision**, and the **Spotify API**.

## Features

* **Face & Emotion Detection:** Uses OpenCV and a Deep Learning model (CNN) to detect faces and classify emotions into 7 categories (Happy, Sad, Angry, Neutral, Fear, Disgust, Surprise).
* **Smart Music Recommendations:** Automatically searches Spotify for songs that match the detected mood (e.g., Upbeat Pop for "Happy", Rock for "Angry", Lofi for "Neutral").
* **Mobile & Web Ready:** Powered by Streamlit, making it accessible from any device (laptop or smartphone) via a browser.
* **Instant Access:** Uses Spotify Client Credentials flow, so no user login is required to get recommendations.

## Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **Computer Vision:** OpenCV (`cv2`)
* **AI/Deep Learning:** TensorFlow & Keras
* **Music Data:** Spotipy (Spotify Web API)
* **Language:** Python 3.x

## Project Structure

```text
mood-music-player/
│
├── app.py                     # The main application script
├── emotion_model.hdf5         # Pre-trained CNN model for emotion recognition
├── requirements.txt           # List of Python dependencies
└── README.md                  # Project documentation
