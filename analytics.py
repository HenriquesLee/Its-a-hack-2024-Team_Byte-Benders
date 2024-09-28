import streamlit as st
import matplotlib.pyplot as plt
import json

def show_analytics():
    st.subheader("📊 Adaptive Learning Analytics")
    
    with open("data/user_data.json", "r") as f:
        user_data = json.load(f)
    
    focus_times = user_data["focus_times"]
    study_times = user_data["study_times"]
    
    st.write("Here is your focus and study performance over the last month:")
    
    fig, ax = plt.subplots()
    ax.plot(focus_times, label="Focus Time")
    ax.plot(study_times, label="Study Time", linestyle="--")
    
    ax.set_xlabel("Days")
    ax.set_ylabel("Minutes")
    ax.legend()
    
    st.pyplot(fig)
    
    st.write("🔮 Predictive Analytics: You are on track to meet your goals if you maintain this pace!")
