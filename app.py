import streamlit as st
import requests
from PIL import Image

image = Image.open("logo.png")

st.markdown("<h1 style='text-align: center; color: black;'>Welcome to:", unsafe_allow_html=True)
st.image(image)

slider = st.slider("How are you feeling today on a scale of 1-10 (1 being the worst and 10 being the best)", min_value=1, max_value=5, value=10, step=1)
st.write(slider)

if slider < 8:
    st.text("Good luck on your Health journey! Let's start by talking about yourself")
else:
    st.text("Let's start by talking about yourself")

name = st.text_input("What is your name")

age = st.number_input("Enter your age", min_value=1, max_value =100)

hobbies = st.text_area("What do you like to do/What are your hobbies")

if name != "":
    st.markdown(
        "Hello " + name + "! " + "Continue answering these questions for the improvement of your mental health."
    )

question = st.checkbox("Are you feeling better after answering these questions?")

audio_formats = ['flv', 'mp3', 'ogg', 'raw', 'wav']


st.title("What's on your mind?")

write_about = st.text_area("Write about it")
audio_file = st.file_uploader("Or upload an audio file", audio_formats, accept_multiple_files=False)


url = "https://api.apilayer.com/text_to_emotion"

payload = write_about.encode("utf-8")
headers= {
  "apikey": "bATA7o2s9ZV8Iz1R4QtKdMpVJ1XxvYQ9"
}

if write_about != "":
    response = requests.request("POST", url, headers=headers, data = payload)
    status_code = response.status_code
    result = response.text
    st.write(result)

st.write("If you need to talk to someone about your problems, please check out: https://checkpointorg.com/global/")

st.subheader("Your feeling statistics based on your notes")

select_item = st.selectbox("Choose a Feeling", ("-", "Happy", "Angry", "Surprise", "Sad", "Fear") )
select_date = st.selectbox("Choose time period", ("-", "Last Week", "Last Month", "Last Year"))

if select_item == "Happy" and select_date == "Last Week":
    st.title("Happy Level: 92%")

if select_item == "Happy" and select_date == "Last Month":
    st.title("Happy Level: 84%")

if select_item == "Happy" and select_date == "Last Year":
    st.title("Happy Level: 86%")

if select_item == "Angry":
    st.title("Anger Level: 24%")

if select_item == "Surprise" and select_date == "Last Week":
    st.title("Surprise Level: 3%")

if select_item == "Surprise" and select_date == "Last Month":
    st.title("Surprise Level: 6%")

if select_item == "Surprise" and select_date == "Last Year":
    st.title("Surprise Level: 8%")

if select_item == "Sad" and select_date == "Last Week":
    st.title("Sad Level: 30%")

if select_item == "Sad" and select_date == "Last Month":
    st.title("Sad Level: 32%")

if select_item == "Sad" and select_date == "Last Year":
    st.title("Sad Level: 35%")

if select_item == "Fear" and select_date == "Last Week":
    st.title("Sad Level: 56%")

if select_item == "Fear" and select_date == "Last Month":
    st.title("Sad Level: 64%")

if select_item == "Fear" and select_date == "Last Year":
    st.title("Sad Level: 70%")



