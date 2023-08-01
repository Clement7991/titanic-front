import streamlit as st
from PIL import Image
import requests

CSS = """
h1 {
    color: black;
}
.stApp {
    background-image: url(https://wallpapercave.com/wp/wp3579042.jpg);
    background-size: cover;
}
"""

st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)


'''
# **A** titanic **mistake** **?**
'''

st.markdown("""
Imagine this is 1912.

You just bought a ticket to board the biggest cruise ship ever made.

Although you aren't a fan of being on the sea or in the water, you were told this ship was unsinkable.

But is it ?

Enter your information below to find out whether you are likely to suffer Jack's fate or have a warm seat on the plank next to Rose.
""")

with st.form(key='params_for_api'):

    # PassengerId = st.number_input('Passenger ID:')
    ticket_class = st.selectbox('Class:', ['1', '2', '3'])
    # name = st.text_input('Full name:')
    sex = st.selectbox('Sex:', ['male', 'female'])
    age = st.number_input('Age:')
    sibs = st.number_input('Number of siblings or spouses onboard:')
    parch = st.number_input('Number of parents or children onboard:')
    # ticket_number = st.text_input('Ticket number:')
    ticket_fare = st.number_input('Ticket fare:')
    # cabine_number = st.text_input('Cabin number:')
    port = st.selectbox('Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton):', ['C', 'Q', 'S'])

    st.form_submit_button('Make prediction')

params = dict(
    ticket_class=ticket_class,
    sex=sex,
    sibs=sibs,
    parch=parch,
    ticket_fare=ticket_fare,
    port=port
)

url = "https://titanic-mistake-yrrvdagiva-ew.a.run.app/predict"

response= requests.get(url, params=params)

prediction = response.json()

st.header("I wouldn't board if I were you...")

# if prediction == "Do not board whatever you do!":
#     st.header("I wouldn't board if I were you...")
#     sinking_image = Image.open('titanic_sinking.jpg')
#     st.image(sinking_image, use_column_width=True)

# else:
#     st.header('There will be space for you on the safety boat! Welcome aboard!')
#     welcome_image = Image.open('welcome.webp')
#     st.image(welcome_image, use_column_width=True)
