import streamlit as st

image_url = "https://unsplash.com/photos/WLUHO9A_xik/download?force=true&w=640"
st.image(image_url, caption='Beautiful Landscape')

audio_url = "https://freemusicarchive.org/track/love-in-the-abstract/download"
st.audio(audio_url, format='audio/mp3')

video_url = "https://pixabay.com/videos/download/video-211/download.mp4"
st.video(video_url)
