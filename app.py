import streamlit as st
from my_pages import home, image_comprehension, grammar, translation

PAGES = {
    "Home": home,
    "Image Comprehension": image_comprehension,
    "Grammar": grammar,
    "Reading and Translation": translation
}

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    page.app()

if __name__ == "__main__":
    main()