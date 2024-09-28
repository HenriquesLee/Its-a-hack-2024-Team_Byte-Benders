import streamlit as st

st.title("👥 Meet the Team")

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
### The NeuroSync Team

NeuroSync was built by a passionate group of AI developers, designers, and engineers. Below is the core team that made this possible.
""")

# Define a reusable function to display team members
def display_team_member(name, role, linkedin_url, github_url):
    """Display team member's details in a structured format"""
    st.subheader(name)
    st.write(f"**Role**: {role}")
    st.write(f"[LinkedIn]({linkedin_url}) | [GitHub]({github_url})")
    st.markdown("---")  # Add a divider after each team member

# Display team members (you can replace these placeholders with actual details)
display_team_member(
    name="Lee Henriques",
    role="AI/ML Developer, Project Lead",
    linkedin_url="https://www.linkedin.com/in/lee-henriques/",
    github_url="https://github.com/HenriquesLee"
)

display_team_member(
    name="Priti Singh",
    role="Frontend Developer",
    linkedin_url="https://www.linkedin.com/in/priti-singh-aba9602ba/",
    github_url="https://github.com/pritisingh-09"
)

display_team_member(
    name="Yash Ganar",
    role="Backend Developer",
    linkedin_url="https://www.linkedin.com/in/yash-ganar-379b1621b/",
    github_url="https://github.com/yashganar90"
)

display_team_member(
    name="Sudheesh Shetty",
    role="Frontend Developer",
    linkedin_url="https://www.linkedin.com/in/sudheesh-shetty/",
    github_url="https://github.com/Sudheesh-07"
)
