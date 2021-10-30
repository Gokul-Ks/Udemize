import streamlit as st
import streamlit.components.v1 as stc

import pandas as pd


#Load Dataset

def load_data(data):
    df = pd.read_csv(data)
    return df

def main():

    st.title("Course Recommendation App")

    menu = ["Home", "Recommend", "About"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")

    elif choice == "Recommend":
        st.subheader("Recommend Courses")
        search_term = st.text_input("Search")
        num_of_rec = st.sidebar.number_input("Number", 4 , 30, 7)
        if st.button("Recommend"):
            if search_term is not None:
                pass
            

    else:
        st.subheader("About")
        st.text("Built for Students and Avid Learners")

if __name__ == "__main__":
    main()
