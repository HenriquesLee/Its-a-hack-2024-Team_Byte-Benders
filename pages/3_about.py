import streamlit as st

st.title("ℹ️ About NeuroSync")
# Set the background image using HTML and CSS
background_image = """
<style>
[data-testid="stSidebarContent"] {
    background-image: linear-gradient(to bottom right, #290e47, #341c5c);
}
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://media1.tenor.com/m/HkBmWN8onyUAAAAC/bg.gif");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)

st.write("""
### What is NeuroSync?
NeuroSync is a personalized AI-driven tool designed to help users maximize productivity, improve focus, and achieve their daily goals. NeuroSync was born out of the need for a smarter, more adaptive tool to help students, professionals, and anyone who struggles with time management and productivity.

The unique aspect of NeuroSync is that it uses **AI** to provide customized assistance based on user input. Whether it's helping to plan a study schedule or offering motivational support, NeuroSync is built to understand your needs and adapt accordingly.

---

### Why NeuroSync?
In a world of endless distractions and packed schedules, it's easy to lose focus. The creators of NeuroSync saw an opportunity to harness the power of AI to build a tool that not only tracks progress but actively helps the user get better at what they do.

Whether you're preparing for a major exam or trying to get through your workday, NeuroSync can help you:
- **Stay on track**: Set and achieve daily, weekly, and long-term goals.
- **Feel motivated**: Get personalized motivational messages when you're feeling unproductive or demotivated.
- **Plan effectively**: Use AI-driven suggestions to optimize your schedule.

---

### Inspiration:
The inspiration for NeuroSync came from observing how students and professionals alike face similar productivity challenges. Our team wanted to build something that isn't just another task manager but a complete productivity solution powered by artificial intelligence.
""")
