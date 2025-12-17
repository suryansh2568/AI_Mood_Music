## AI Mood Music Player

A smart AI-powered web application that detects your current emotion from your facial expression and recommends the perfect Spotify song to match your mood.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Spotify](https://img.shields.io/badge/Spotify-1ED760?style=for-the-badge&logo=spotify&logoColor=white)

---

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
