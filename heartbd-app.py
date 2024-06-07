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
url = 'http://127.0.0.1:8000/predict'

# params with default values
params = {'0_pre-RR': 163 ,
          '0_post-RR': 165 ,
          '0_pPeak': 0.069610222,
          '0_tPeak': -0.083280601,
          '0_rPeak': 0.614133158,
          '0_sPeak': -0.392761319,
          '0_qPeak': 0.047159284,
          '0_qrs_interval': 15,
          '0_pq_interval': 2,
          '0_qt_interval': 27,
          '0_st_interval': 10,
          '0_qrs_morph0': 0.047159284,
          '0_qrs_morph1': 0.146934163,
          '0_qrs_morph2': 0.506484864,
          '0_qrs_morph3': 0.550094976,
          '0_qrs_morph4': -0.053038448,
          '1_pre-RR': 163,
          '1_post-RR': 165,
          '1_pPeak': -0.013397687,
          '1_tPeak': 0.204003068,
          '1_rPeak': 0.123921531,
          '1_sPeak': -0.421341864,
          '1_qPeak': -0.023370488,
          '1_qrs_interval': 14,
          '1_pq_interval': 3,
          '1_qt_interval': 23,
          '1_st_interval': 6,
          '1_qrs_morph0': -0.023370488,
          '1_qrs_morph1': -0.01165031,
          '1_qrs_morph2': 0.082607626,
          '1_qrs_morph3': 0.101372903,
          '1_qrs_morph4': -0.183386854}

response = requests.get(url, params=params)

# Output results
st.markdown('''
## The results are in...
''')
st.write(f"{response.json()}")
