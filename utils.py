import streamlit as st

def start_timer(duration):
    """
    Starts a countdown timer for the given duration in seconds and shows the progress in Streamlit.
    """
    while duration:
        mins, secs = divmod(duration, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        st.write(f"Time Remaining: {timeformat}")
        time.sleep(1)
        duration -= 1
    st.write("Timer completed!")

def notify(message, sound_path):
    """
    Displays a notification message and plays a sound file using Streamlit's audio player.
    """
    st.success(message)
    
    # Play the notification sound using Streamlit's audio player
    try:
        audio_file = open(sound_path, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
    except Exception as e:
        st.error(f"Error playing sound: {e}")
