import streamlit as st
import requests

'''
# A **titanic** mistake ?
'''

st.markdown("""
Imagine this is 1912.

You just bought a ticket to board the biggest cruise ship ever made.

Although you aren't a fan of being on the sea or in the water, you were told this ship was unsinkable.

But is it ?

Enter your information below to find out whether you are Jack or Rose.
""")

with st.form(key='params_for_api'):

    PassengerId = st.number_input('Passenger ID:')
    ticket_class = st.number_input('Ticket class:')
    name = st.text_input('Full name:')
    sex = st.selectbox('Sex:', ['male', 'female'])
    age = st.number_input('Age:')
    sibs = st.number_input('Number of siblings or spouses onboard:')
    parch = st.number_input('Number of parents or children onboard:')
    ticket_number = st.text_input('Ticket number:')
    ticket_fare = st.number_input('Ticket fare:')
    cabine_number = st.text_input('Cabin number:')
    port = st.selectbox('Port of embarkation (S, C or Q):', ['S', 'C', 'Q'])

    st.form_submit_button('Make prediction')

params = dict(
    PassengerId,
    ticket_class,
    name,
    sex,
    sibs,
    parch,
    ticket_number,
    ticket_fare,
    cabine_number,
    port
)

url = 'http://localhost:8000/predict'
# ?PassengerId={PassengerId}&Pclass={ticket_class}&Name={name}&Sex={name}&Age={age}&Sibs={sibs}&Parch={parch}&Ticket={ticket_number}&Fare={ticket_fare}&Cabin={cabine_number}&Embarked={port}

response= requests.get(url, params)

prediction = response.json()

st.header(f'{prediction}')
