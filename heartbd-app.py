import streamlit as st
import requests

'''
# Heart Beat Decoder

## A machine learning model to classify ECG results
'''

st.markdown('''
## First, please record or upload your ecg results and indicate their format:
''')

# input_columns = st.columns(2)
st.button("Upload ECG results")
st.button("Analyze my results")


# Call API to run model on input data
url = 'http://127.0.0.1:8000/'
params = {}
response = requests.get(url, params=params)

# Output results
st.markdown('''
## The results are in...
''')
st.write(f"{response.json()}")
