# Mood Music Player

### *Your Face. Your Mood. Your Music.*

A smart AI-powered web application that detects your real-time emotion from facial expressions and instantly recommends the perfect Spotify track to match your vibe. No login required—just snap and play.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Spotify](https://img.shields.io/badge/Spotify-1ED760?style=for-the-badge&logo=spotify&logoColor=white)

---

## Project Overview

The **Mood Music Player** bridges the gap between computer vision and music recommendation. Instead of manually searching for a playlist, this app uses a Deep Learning model to "see" how you feel.

Whether you're happy, sad, or just chill, the app analyzes your facial features and queries the Spotify API to deliver a song that resonates with your current emotional state.

### Key Features

* **Real-Time Emotion Detection:** Utilizing a CNN (Convolutional Neural Network) trained on thousands of facial images to classify 7 distinct emotions: *Happy, Sad, Angry, Neutral, Fear, Disgust, Surprise*.
* **Smart Music Mapping:** Intelligent logic maps specific emotions to musical genres (e.g., *Happy* → Upbeat Pop, *Angry* → Heavy Rock, *Sad* → Acoustic Piano).
* **Instant Playback:** Powered by **Spotify Client Credentials**, allowing instant song retrieval without requiring users to log in.
* **Cross-Platform:** Built with **Streamlit**, making it fully responsive and accessible on both desktop and mobile browsers.
* **Privacy-First:** All image processing happens in volatile memory; no user photos are ever saved or stored.

---

## Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | Streamlit | Rapid web application framework for Python. |
| **Computer Vision** | OpenCV (`cv2`) | Face detection using Haar Cascades. |
| **AI Model** | TensorFlow / Keras | Pre-trained CNN model (`emotion_model.hdf5`) for emotion classification. |
| **Music Data** | Spotipy | Python wrapper for the Spotify Web API. |
| **Language** | Python 3.x | Core programming language. |

---

## Project Structure

```text
mood-music-player/
│
├── app.py                     # Main application script (Streamlit)
├── emotion_model.hdf5         # Pre-trained AI model for emotion detection
├── requirements.txt           # Dependencies list for Cloud Deployment
├── haarcascade_frontalface_default.xml # Face detection XML (optional if using cv2.data)
└── README.md                  # Project documentation
```

---

## Setup & Installation (Local)

Follow these steps to run the app on your own machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/mood-music-player.git](https://github.com/your-username/mood-music-player.git)
cd mood-music-player
```

### 2. Install Dependencies
Ensure you have Python installed (3.8 - 3.11 recommended).
```bash
pip install -r requirements.txt
```

### 3. Configure Spotify Keys
To fetch songs, you need API keys from Spotify (free).
1.  Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2.  Log in and create a new app.
3.  Copy your **Client ID** and **Client Secret**.
4.  Open `app.py` and replace the placeholder keys:
    ```python
    CLIENT_ID = 'your_actual_client_id'
    CLIENT_SECRET = 'your_actual_client_secret'
    ```

### 4. Run the App
```bash
streamlit run app.py
```
The app will open automatically in your browser at `http://localhost:8501`.

---

## ☁️ Deployment Guide (Streamlit Cloud)

This app is optimized for the cloud. To make it accessible to everyone:

1.  **Push to GitHub:** Ensure `app.py`, `requirements.txt`, and `emotion_model.hdf5` are in your repository.
2.  **Sign in to Streamlit Cloud:** Go to [share.streamlit.io](https://share.streamlit.io/).
3.  **Deploy:** Connect your GitHub account and select your repository.
4.  **Launch:** Click "Deploy". The app will be live in minutes!

**Important for Cloud:**
Ensure your `requirements.txt` includes `opencv-python-headless` instead of `opencv-python`. This prevents server crashes due to missing video drivers.

---

## Future Roadmap

* [ ] **Playlist Support:** Play full playlists instead of single tracks.
* [ ] **User Login:** Allow users to log in to save songs to their actual library.
* [ ] **Genre Selection:** Let users pick their preferred genre (e.g., Bollywood vs. Hollywood) before scanning.
* [ ] **Mood History:** A visual graph showing your mood trends over time.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

### Author
**Suryansh**
*Computer Science Major & AI Enthusiast*
