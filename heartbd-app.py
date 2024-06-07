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

params = {'0_pre-RR', '0_post-RR', '0_pPeak', '0_tPeak', '0_rPeak', '0_sPeak',
          '0_qPeak', '0_qrs_interval', '0_pq_interval', '0_qt_interval',
          '0_st_interval', '0_qrs_morph0', '0_qrs_morph1', '0_qrs_morph2',
          '0_qrs_morph3', '0_qrs_morph4', '1_pre-RR', '1_post-RR', '1_pPeak',
          '1_tPeak', '1_rPeak', '1_sPeak', '1_qPeak', '1_qrs_interval',
          '1_pq_interval', '1_qt_interval', '1_st_interval', '1_qrs_morph0',
          '1_qrs_morph1', '1_qrs_morph2', '1_qrs_morph3', '1_qrs_morph4'}

response = requests.get(url, params=params)

# Output results
st.markdown('''
## The results are in...
''')
st.write(f"{response.json()}")
