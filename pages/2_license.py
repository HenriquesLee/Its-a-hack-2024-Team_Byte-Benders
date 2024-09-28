import streamlit as st

st.title("📜 License - GNU General Public License v3.0")

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
**NeuroSync** is open-sourced under the **GNU General Public License v3.0 (GPL-3.0)**. This license guarantees end users the freedom to run, study, share, and modify the software.

### Key Points of the License:
- **Freedom to Use**: You have the right to use the software for any purpose.
- **Freedom to Modify**: You can study how the program works and adapt it to your needs.
- **Freedom to Distribute Copies**: You can redistribute copies of the software and share it with others.
- **Freedom to Improve**: You can improve the program and release your improvements to the public, with the stipulation that the same freedoms apply to others.

---

### Full License:
The full license text can be found [here](https://www.gnu.org/licenses/gpl-3.0.en.html).

""")
