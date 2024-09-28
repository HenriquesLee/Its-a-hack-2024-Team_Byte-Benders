import streamlit as st
import time
from utils import notify

# Function to start the timer and return remaining time
def start_timer(duration, paused):
    """Start a countdown timer for the specified duration in seconds."""
    start_time = time.time()
    timer_display = st.empty()  # Create an empty placeholder for the timer display

    while duration > 0:
        if paused[0]:  # Check if the timer is paused
            time.sleep(0.1)  # Sleep briefly to reduce CPU usage
            continue

        elapsed = time.time() - start_time
        remaining = duration - elapsed
        if remaining <= 0:
            timer_display.write("Time's up!")
            notify("Focus Session Completed! Take a Break!", "assets/success.mp3")
            return 0

        mins, secs = divmod(int(remaining), 60)
        timer = f'{mins:02}:{secs:02}'
        timer_display.write(f"Time Remaining: {timer}")  # Update the display

        time.sleep(1)  # Wait for one second before updating

        if st.session_state.stop:  # Check if the stop button was pressed
            timer_display.write("Focus session stopped!")
            return -1

    return remaining

def start_focus_session():
    st.subheader("🔍 AI-Driven Focus Mode")
    
    # Slider for focus and break durations
    duration = st.slider("Set Focus Duration (minutes)", 15, 120, 25)
    break_duration = st.slider("Set Break Duration (minutes)", 5, 20, 5)
    
    # Initialize session state variables
    if 'paused' not in st.session_state:
        st.session_state.paused = [False]
    if 'stop' not in st.session_state:
        st.session_state.stop = False
    if 'timer_running' not in st.session_state:
        st.session_state.timer_running = False  # Track if the timer is currently running

    start_button = st.button("Start Focus Session")

    if start_button:
        st.session_state.timer_running = True  # Set timer running flag
        st.write("Focus session started!")
        
        # Run the timer
        remaining_time = start_timer(duration * 60, st.session_state.paused)
        
        if remaining_time == 0:  # If time is up, start the break timer
            st.write("Break time started!")
            start_timer(break_duration * 60, st.session_state.paused)
            notify("Break Over! Back to Work!", "assets/focus_start.mp3")
        
        # Reset the stop flag
        st.session_state.stop = False
        st.session_state.timer_running = False  # Reset timer running flag
    

    if st.button("Stop Timer"):
        st.session_state.stop = True  # Set stop flag
        st.write("Timer will stop after current countdown.")

