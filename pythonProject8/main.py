import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")



lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_tfb3estd.json")
img_deepfake = Image.open("Images/Deepfake.jpg")
img_jarvis = Image.open("Images/jarvis.jpg")

with st.container():
    st.subheader("Hi I am Sanyam :wave:")
    st.title("A coding enthusiast")
    st.write("I am passionate about finding ways in Python to make life easier")
    st.write("[Learn More >](https://www.linkedin.com/in/sanyam-jain-a5a15a220)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write("##")
        st.write(
            """
            - I am currently pursuing dual degree 
              - First being BSc in Data Science snd Programming from IITM
              - Second being BTech in CSE from MUJ
            - I am currently into researches regarding ML
            - I am a huge anime weeb and a bingewatcher
            - Tech enthusiast 
            """
            )
    with right_column:
        st_lottie(lottie_coding)

    with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
        image_column, text_column = st.columns((2,6))
        with image_column:
            st.image(img_jarvis)

        with text_column:
            st.subheader("Jarvis Automated Voice Assistant")
            st.write(
                """
                - Made a voice assistant jarvis which can fully automate tasks on your desktop
                - From restarting to shutdown, from greeting you to open any youtube video automatically
                - from responding you to emailing anyone , it can do anything and also has a gui
                
                
                """
                )
            st.markdown("[Github repo link](https://github.com/Sj0605-DataSci/Jarvis-Voice-Assistant)")

    with st.container():
        image_column, text_column = st.columns((2,6))
        with image_column:
            st.image(img_deepfake)

        with text_column:
            st.subheader("Deepfake creation")
            st.write(
                """
                - Deepfakes (a portmanteau of "deep learning" and "fake"[1]) are synthetic media[2] in which a person in an existing image or video is replaced with someone else's likeness. 
                - While the act of creating fake content is not new, deepfakes leverage powerful techniques from machine learning and artificial intelligence to manipulate or generate visual and audio content that can more easily deceive


                """
            )
            st.markdown("[Github repo link](https://github.com/Sj0605-DataSci/DeepFake)")

    with st.container():
        st.write("---")
        st.subheader("Get in touch with me!")
        st.write("##")

        contact_form = """
        <form action="https://formsubmit.co/sanyam0605@email.com" method="POST">
     <input type = "hidden" name="_captcha" value="false">   
     <input type="text" name="name"  placeholder = "Your Name" required>
     <input type="email" name="email" placeholder = "Your Email" required>
     <textarea name="message" placeholder = "Your Message here" required></textarea>
     <button type="submit">Send</button>
        </form>
        
        """
        left_column,right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
